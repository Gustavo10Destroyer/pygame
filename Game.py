class Game:
    def __init__(self, pygame, screen):
        self.running = True
        self.__loadeds__ = []
        self.__pygame__ = pygame
        self.__screen__ = screen

    def __loaded__(self, module):
        return (module in self.__loadeds__)

    def __use__(self, module):
        if not self.__loaded__(module):
            module(self)
            self.__loadeds__.append(module)
            print("[INIT]: 1 módulo foi carregado!")

    def __require__(self, module):
        if not self.__loaded__(module):
            print("[ERRO]: O módulo não está carregado!")

    def quit(self):
        print("[INFO]: Saindo...")
        self.running = False