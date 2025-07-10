import pygame
import sys


pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

displaysurface=pygame.display.set_mode((screen_width,screen_height))
image=pygame.transform.scale(
    pygame.image.load('hehe.jpg').convert_alpha(), (200,200))
rect=image.get_rect(center=(screen_width//2,
                                            screen_height//2-30))

pygame.display.set_caption("My first game screen")


background_color = (58, 58, 58) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)
    displaysurface.blit(image,rect)
    pygame.display.flip()

pygame.quit()
sys.exit()