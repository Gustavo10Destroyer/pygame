import socket
from Game import Game

class Network:
    def __init__(self, game):
        if type(game) != Game:
            return print("[ERRO]: Esse módulo só pode ser construído pelo jogo!")
        else:
            self.__game__ = game