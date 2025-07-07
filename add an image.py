import pygame

pygame.init()
screenwidth, screenheight = 500,500

displaysurface=pygame.display.set_mode((screenwidth,screenheight))
pygame.display.set_caption('Adding image and background image')

backgroundimage=pygame.transform.scale(
    pygame.image.load('background.jpg').convert(),
    (screenwidth, screenheight))

penguinimage=pygame.transform.scale(
    pygame.image.load('hello penguin.jpg').convert_alpha(), (200,300))
penguin_rect=penguinimage.get_rect(center=(screenwidth//2,
                                            screenheight//2-30))

text=pygame.font.Font(None, 36).render('Hello world', True,
                                       pygame.Color('black'))
textrect=text.get_rect(center=(screenwidth//2, screenheight//2+110))

def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
    
        displaysurface.blit(backgroundimage,(0,0))
        displaysurface.blit(penguinimage,penguin_rect)
        displaysurface.blit(text, textrect)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__=='__main__':
    game_loop()