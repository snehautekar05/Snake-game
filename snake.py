import pygame
from pygame.locals import *

def draw_block():
    surface.fill((100, 100, 5))
    surface.blit(block, (block_x, block_y))
    pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    
    surface = pygame.display.set_mode((500,500))
    surface.fill((100, 100, 5))
    
    block = pygame.image.load("C:/Users/SNEHA SANDEEP UTEKAR/OneDrive/Desktop/resources/block.jpg").convert() # Put your images location here.
    block_x = 100
    block_y = 100
    
    surface.blit(block, (block_x, block_y))
    
    pygame.display.flip()
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    
                if event.key == K_LEFT:
                    block_x -= 10
                    draw_block()
                    
                if event.key == K_RIGHT:
                    block_x += 10
                    draw_block()
                    
                if event.key == K_UP:
                    block_y -= 10
                    draw_block()
                    
                if event.key == K_DOWN:
                    block_y += 10
                    draw_block()
                
            elif event.type == QUIT:
                running = False



