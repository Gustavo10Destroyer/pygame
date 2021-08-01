import uuid
from Game import Game
from Network import Network

class Players:
    def __init__(self, game, localPlayer):
        if type(game) != Game:
            return print("[ERRO]: Esse módulo só pode ser construído pelo módulo Game!")
        else:
            self.__players__ = [localPlayer]
            self.LocalPlayer = localPlayer

    def getPlayers(self):
        return self.__players__
    
    def addPlayer(self, network):
        if type(network) != Network:
            return print("[ERRO]: Esse módulo só pode ser construído pelo módulo Network!")

class Player:
    def __init__(self, game):
        if type(game) != Game:
            return print("[ERRO]: Esse módulo só pode ser construído pelo módulo Game!")
        else:
            self.__name__ = ""
            self.__game__ = game
            self.__uuid__ = str(uuid.uuid4())

            game.players = Players(game, self)
    
    def draw(self):
        pygame = self.__game__.__pygame__
        screen = self.__game__.__screen__

        pygame.draw.circle(screen, (0, 170, 0), (100, 100), 75)
        pygame.display.flip()

    def getName(self):
        return self.__name__
    
    def setName(self, name):
        if type(name) == str:
            self.__name__ = name
        else:
            print("[ERRO]: O tipo do nome deve ser uma String!")