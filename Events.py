from Game import Game
from Player import Player

class Listener:
    def __init__(self, game):
        if type(game) != Game:
            return print("[ERRO]: Esse módulo só pode ser construído pelo módulo Game!")
        else:
            game.listener = self
            self.__game__ = game
            game.__listeners__ = {}
    
    def __addListener__(self, listener):
        try:
            self.__game__.__listeners__[listener["Event"]].append(listener["Callback"])
        except KeyError:
            self.__game__.__listeners__[listener["Event"]] = []
            self.__game__.__listeners__[listener["Event"]].append(listener["Callback"])

    def onPlayerJoin(self, callback):
        event = {
            "Event": "PlayerJoin",
            "Callback": callback
        }

        self.__addListener__(event)
    
    def onPlayerUpdate(self, callback):
        event = {
            "Event": "PlayerUpdate",
            "Callback": callback
        }

        self.__addListener__(event)

    def onPlayerLeave(self, callback):
        event = {
            "Event": "PlayerLeave",
            "Callback": callback
        }

        self.__addListener__(event)

class Emitter:
    def __init__(self, game):
        if type(game) != Game:
            return print("[ERRO]: Esse módulo só pode ser construído pelo módulo Game!")
        else:
            game.emitter = self
            self.__game__ = game
            game.__require__(Listener)

    def __emit__(self, event):
        try:
            if self.__game__.__listeners__[event["Event"]]:
                for i in self.__game__.__listeners__[event["Event"]]:
                    i(event["Data"])

        except KeyError:
            print("KeyError: Invalid key ... " + str(event["Event"]))

    def playerUpdate(self, player):
        if type(player) != Player:
            return print("[ERRO]: O objeto 'player' precisa ser uma instância de Player!")
        else:
            event = {
                "Event": "PlayerUpdate",
                "Data": {
                    "Player": player
                }
            }

            self.__emit__(event)