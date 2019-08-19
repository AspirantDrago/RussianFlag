import pygame


pygame.init()
size = width, height = 480, 400
screen = pygame.display.set_mode(size)

def draw():
    screen.fill([255, 255, 255])
    pygame.display.set_caption("Российский флаг")
    # Рисуем флагшток
    flagpole_color = [226, 132, 50]
    flagpole_rect = [(40, 20), (5, height - 20 * 2)]
    pygame.draw.rect(screen, flagpole_color, flagpole_rect)

draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
