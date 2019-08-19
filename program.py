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
    # Рисуем синий сегмент (цвет по ГОСТу Р 51130-98)
    segment_blue_color = [0, 57, 166]
    segment_blue_rect = [(30, 30 + 2 * 40), (9 * 40, 2 * 40)]
    pygame.draw.rect(screen, segment_blue_color, segment_blue_rect)
    # Рисуем красный сегмент (цвет по ГОСТу Р 51130-98)
    segment_red_color = [213, 43, 30]
    segment_red_rect = [(30, 30 + 2 * 2 * 40), (9 * 40, 2 * 40)]
    pygame.draw.rect(screen, segment_red_color, segment_red_rect)
    # Рисуем границы флага
    segment_border_color = [0] * 3
    segment_border_rect = [(30, 30), (9 * 40, 3 * 2 * 40)]
    pygame.draw.rect(screen, segment_border_color, segment_border_rect, 1)


draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()
