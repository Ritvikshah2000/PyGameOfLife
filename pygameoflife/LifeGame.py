import sys
import pygame

boardSize = width, height = 640, 480
deadColor = 0,0,0
aliveColor = 0,255,255

class LifeGame:

    def __init__(self): #init function
        pygame.init()
        self.screen = pygame.display.set_mode(boardSize)

    def clearScreen(self): #clears screen
        self.screen.fill(deadColor)

    def run(self): #run function

        circleRect = pygame.draw.circle(self.screen, aliveColor, (50,50), 5, 0) #(surface, color, pos, radius, width)
        print(type(circleRect)) #prints class
        print(circleRect) #prints dimensions of circle
        # screen.blit(ball,ballrect) #blit means to draw
        pygame.display.flip()  # pushes the screen to video memory



        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            self.screen.fill(deadColor)




if __name__ == '__main__':
    game = LifeGame()  # new instance of game
    game.run()  # run game
