import pygame


pygame.init()
size = width, height = 480, 400
screen = pygame.display.set_mode(size)

def draw():
    screen.fill([255, 255, 255])
    pygame.display.set_caption("Российский флаг")

draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
