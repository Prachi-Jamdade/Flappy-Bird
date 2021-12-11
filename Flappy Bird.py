import random # for generating random numbers
import sys # use sys.exit to exit the game
import pygame
from pygame.locals import *

def base_movement(window, base_img, var_x):
    window.blit(base_img, (var_x, 512 - 75))

    #second window
    window.blit(base_img, (var_x + 200, 512 - 75))

def bird_movement(window, bird_img, bird_rect):
    window.blit(bird_img, bird_rect)

def pipe_movement(window, pipe_img, pipes):
    for pipe in pipes:
        pipe.centerx -= 5

    for pipe in pipes:
        window.blit(pipe_img, pipe)

def collision(pipes, bird_rect):
    for pipe in pipes:
        if pipe.colliderect(bird_rect):
            print("Collided")

        if bird_rect.top <= -10:
            print("Exceeded Upper Limit...")

        if bird_rect.bottom >= (512 - 75):
            print("Exceeded Lower Limit...")


def game_build():
    pygame.init() #initialize all pygame's modules
    pygame.display.set_caption("The Flappy Bird Game") # use to set a caption
    window = pygame.display.set_mode((288, 512)) # creates a screen for us

    #background
    back_img = pygame.image.load(r'C:\Users\Prachi S Jamdade\Pictures\resources\back.jpg').convert()

    #base
    base_img = pygame.image.load(r'C:\Users\Prachi S Jamdade\Pictures\resources\base.png').convert_alpha()
    var_x = 0

    #bird
    bird_img = pygame.image.load(r'C:\Users\Prachi S Jamdade\Pictures\resources\bird.jpg').convert_alpha()

    bird_rect = bird_img.get_rect(center=(75, 512/2))
    g_force = 0.3
    bird_new_pos = 0

    #pipes
    # pipe_img = pygame.transform.rotate(pygame.image.load(r'C:\Users\Prachi S Jamdade\Pictures\Screenshots\pipe.png').convert_alpha(), 180)
    pipe_img = pygame.image.load(r'C:\Users\Prachi S Jamdade\Pictures\resources\pipe.png')
    list_of_pipe = []

    TIMER = pygame.USEREVENT
    pygame.time.set_timer(TIMER, 1000)

    #main loop
    clk = pygame.time.Clock()
    while True:
        #event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.type == K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bird_new_pos = 0
                    bird_new_pos -= 0

            if event.type == TIMER:
                random_pipe_height = [200, 250, 300, 350, 400]
                pipes = pipe_img.get_rect(midtop = (290, random.choice(random_pipe_height)))
                list_of_pipe.append(pipes)

        #game logic
        window.blit(back_img, (0, 0))

        #collition detection
        collision(list_of_pipe, bird_rect)

        #pipe movement
        pipe_movement(window, pipe_img, list_of_pipe)

        #base movement
        var_x -= 1
        base_movement(window, base_img, var_x)
        
        if var_x <= -200:
            var_x = 0

        #bird movement
        bird_new_pos += g_force
        bird_rect.centery += bird_new_pos
        bird_movement(window, bird_img, bird_rect)

        #updating
        clk.tick(32)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    game_build()
                
