from typing import Text
import pygame
from network import Network
import pickle
pygame.font.init()

width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255, 255, 255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))
    
    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.heigth:
            return True
        else:
            return False

class pile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.upper_card = None
    
    def show_card(self, win):
        image = pygame.image.load(r'test1.bmp')
        win.blit(image, (0, 0))


def redrawWindow(win, game, p):
    win.fill((128,128,128))
    pass

btn = Button('Draw Card', 50, 500, (0,0,0))

def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print('You are player', player)

    while run:
        clock.tick(60)
        try:
            game = n.send('get')
        except:
            run = False
            print('Could not get game')
            break

        if game.bothWent():
            redrawWindow()
            pygame.time.delay(500)
            try:
                game = n.send('reset')
            except:
                run = False
                print('Could not get game')
                break

            font = pygame.font.SysFont('comicsans', 90)
            if (game.winner() == 1 and player == 1) or (game.winner() == 0 and player == 0):
                text = font.render('You won!', 1, (255,0,0))
            elif game.winner == -1:
                text = font.render('Tie Game!', 1, (255, 0, 0))
            else:
                text = font.render('You lost!', 1, (255, 0, 0))

            win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type -- pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if btn.click(pos) and game.connected():
                    pass
main()