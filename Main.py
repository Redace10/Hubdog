import pygame
import os

# sets basic game features
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

# plays background song repeatedly
pygame.mixer.music.load("The Marching Pirate Spy.mp3")
pygame.mixer.music.play(-1, 0)

dog_images = []
left_images = []
right_images = []
attack_images = []

left1 = pygame.image.load('moving/good/left1.png')
left2 = pygame.image.load('moving/good/left2.png')
left1 = pygame.transform.scale(left1, (135, 115))
left2 = pygame.transform.scale(left2, (135, 115))

right1 = pygame.image.load('moving/good/right1.png')
right2 = pygame.image.load('moving/good/right2.png')
right1 = pygame.transform.scale(right1, (135, 115))
right2 = pygame.transform.scale(right2, (135, 115))

attack1 = pygame.image.load('attack/attack1.png')
attack2 = pygame.image.load('attack/attack1.png')
attack1 = pygame.transform.scale(attack1, (137, 142))
attack2 = pygame.transform.scale(attack2, (137, 142))

map = pygame.image.load('boss battle.png')

left_images.append(left1)
left_images.append(left2)
right_images.append(right1)
right_images.append(right2)
attack_images.append(attack1)
attack_images.append(attack2)

dog_images.append(left_images)
dog_images.append(right_images)
dog_images.append(attack_images)

face = 0
index = 0
dog = dog_images[index]

x_Display = 800
y_Display = 600
gameDisplay = pygame.display.set_mode((x_Display, y_Display))
game_border = (0, 108, 800, 415)

# dog movements and body
movement_speed = 5
x_change = 0
y_change = 0

rect = dog[0].get_rect()

# beginning game features
keepPlaying = True
clock = pygame.time.Clock()

# variables for which side the dog is facing
moveUp = moveDown = moveRight = moveLeft = False
attack = False

while keepPlaying:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepPlaying = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                face = 0
                moveLeft = True
                moveUp = moveDown = moveRight = False
                x_change -= movement_speed
            if event.key == pygame.K_RIGHT:
                face = 1
                moveRight = True
                moveUp = moveDown = moveLeft = False
                x_change += movement_speed
            if event.key == pygame.K_UP:
                moveUp = True
                moveDown = moveRight = moveLeft = False
                y_change -= movement_speed
            if event.key == pygame.K_DOWN:
                moveDown = True
                moveUp = moveRight = moveLeft = False
                y_change += movement_speed
            if event.key == pygame.K_SPACE:
                attack = True
                face = 2
            

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change = 0
                moveLeft = False
            if event.key == pygame.K_RIGHT:
                x_change = 0
                moveRight = False
            if event.key == pygame.K_UP:
                y_change = 0
                moveUp = False
            if event.key == pygame.K_DOWN:
                y_change = 0
                moveDown = False
            if event.key == pygame.K_SPACE:
                attack = False
                face = 0

    if (index == 19):
        index = 0
    else:
        if (moveLeft or moveRight or moveUp or moveDown):
            index += 1

    dog = dog_images[face][index//10]
    if (not attack):
        rect.move_ip(x_change, y_change)
    rect.clamp_ip(game_border)
    gameDisplay.blit(map, (0, 0))
    if (attack):
        gameDisplay.blit(dog, (rect.x, rect.y-30))
    else:
        gameDisplay.blit(dog, rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()