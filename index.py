import pygame
from time import sleep

from Game import Game
from Player import Player
from Network import Network
from Events import Listener, Emitter

pygame.init()

screen = pygame.display.set_mode([600, 300])

game = Game(pygame, screen)
game.__use__(Player)
game.__use__(Network)
game.__use__(Listener)
game.__use__(Emitter)

def onPlayerUpdate(event):
    print("PlayerUpdate fired!")
    print(event["Player"].getName())

localPlayer = game.players.LocalPlayer
localPlayer.setName("Gustavo")

game.listener.onPlayerUpdate(onPlayerUpdate)

while game.running:
    pygame.display.set_caption(localPlayer.getName())
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.quit()
    
    localPlayer.draw()

    sleep(0.1)

pygame.quit()