import pygame
import os

# sets basic game features
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

# plays background song repeatedly
pygame.mixer.music.load("The Marching Pirate Spy.mp3")
pygame.mixer.music.play(-1, 0)

dog_images = []
image1 = pygame.image.load('moving/good/walking1.png')
image2 = pygame.image.load('moving/good/walking2.png')
image1 = pygame.transform.scale(image1, (40, 40))
image2 = pygame.transform.scale(image2, (40, 40))
dog_images.append(image1)
dog_images.append(image2)
index = 0
dog = dog_images[index]

x_Display = 800
y_Display = 600
gameDisplay = pygame.display.set_mode((x_Display, y_Display))
game_border = (0, 108, 800, 415)

# dog movements and body
movement_speed = 10
x_change = 0
y_change = 0

rect = dog.get_rect()

# beginning game features
keepPlaying = True
clock = pygame.time.Clock()

while keepPlaying:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepPlaying = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change -= movement_speed
            if event.key == pygame.K_RIGHT:
                x_change += movement_speed
            if event.key == pygame.K_UP:
                y_change -= movement_speed
            if event.key == pygame.K_DOWN:
                y_change += movement_speed

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_UP:
                y_change = 0
            if event.key == pygame.K_DOWN:
                y_change = 0

    rect.clamp_ip(game_border)
    rect.move_ip(x_change, y_change)
    gameDisplay.blit(dog, rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()