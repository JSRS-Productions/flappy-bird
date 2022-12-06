import pygame
import sys
from pygame import mixer
import random

pygame.init()
mixer.init()

screen_width = 1000
screen_height = 700

bg_image = pygame.image.load("assets1/bg.png")
bg_image = pygame.transform.scale(bg_image,(1000,700))

bird = pygame.image.load("assets1/bird.png")
bird = pygame.transform.scale(bird,(100,80))
bird_rect = bird.get_rect()
bird_rect.center = 100,100
bird_speed = 1


tube = pygame.image.load("assets1/tube1.png")

tube2 = pygame.image.load("assets1/tube2.png")

screen = pygame.display.set_mode((screen_width,screen_height))
mixer.music.load("assets1/bg_sound.mp3")
mixer.music.play(-1)

tubes = []

tubes2 = []

score_counter = 0

periodic_tube_generation = pygame.USEREVENT
pygame.time.set_timer(periodic_tube_generation,3000)

periodic_tube_generation2 = pygame.USEREVENT
pygame.time.set_timer(periodic_tube_generation2,3000)

tube_generate_count = 1
tube_generate_count2 = 1

def generate_tubes():
    global tube_generate_count,tube,tubes

    for tub in range(tube_generate_count):
        tube_y = 0
        tube_x = screen_width
        tube_rect = tube.get_rect()
        tube_rect.y = tube_y
        tube_rect.x = tube_x
        # tube_length = random.randint(100,150)
        tube = pygame.transform.scale(tube,(80,50))
        tubes.append([tube,tube_rect])

def generate_tubes2():
    global tube_generate_count2,tube2,tubes2
    for tub2 in range(tube_generate_count2):
        tube_y2 = 500
        tube_x2 = screen_width
        tube_rect2 = tube.get_rect()
        tube_rect2.y = tube_y2
        tube_rect2.x = tube_x2
        # tube_length2 = random.randint(100,150)
        tube2 = pygame.transform.scale(tube2,(80,50))
        tubes2.append([tube2,tube_rect2])

def display_tube():
    global tubes

    for tub in tubes:
        tube_image_obj = tub[0]
        tube_rect_obj = tub[1]
        
        tube_rect_obj.x += -1
        print(tube_rect_obj.x,tube_rect_obj.y)
        screen.blit(tube_image_obj,tube_rect_obj)
        pygame.draw.rect(screen,(0,0,0),tube_rect_obj)

def display_tube2():
    global tubes2

    for tub2 in tubes2:
        tube_image_obj2 = tub2[0]
        tube_rect_obj2 = tub2[1]

        tube_rect_obj2.x += -1

        screen.blit(tube_image_obj2,tube_rect_obj2)

def check_collision():
    global tubes,bird_rect,tube_generate_count,tube_generate_count2

    for tube_item in tubes:
        tube_rect_obj = tube_item[1]

        if bird_rect.colliderect(tube_rect_obj):
            print(" upper collision")
            tube_generate_count = 0
            tube_generate_count2 = 0
            sound_2 = pygame.mixer.Sound("assets1/game_over.wav")
            mixer.Channel(2).play(sound_2)

def check_collision2():
    global tubes2,bird_rect,tube_generate_count,tube_generate_count2

    for tube_item2 in tubes2:
        tube_rect_obj2 = tube_item2[1]

        if bird_rect.colliderect(tube_rect_obj2):
            print(" lower collision")
            tube_generate_count=0
            tube_generate_count2 = 0
            sound_3 = pygame.mixer.Sound("assets1/game_over.wav")
            mixer.Channel(3).play(sound_3)

def write_text(text,x,y,size=5,color=(255,255,255)):

    font = pygame.font.Font('freesansbold.ttf',size)
    text_obj = font.render(text,True,color,screen.get_alpha())
    textRect = text_obj.get_rect()
    textRect.center = (x,y)
    screen.blit(text_obj,textRect)

def check_points():
    global score_counter,bird_rect

    if bird_rect.x > 0:
        score_counter+=1
    elif bird_rect.x > 0:
        score_counter+=1

def display_scores():
         write_text(str(score_counter),525,100,50)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
                sys.exit()

        if event.type==periodic_tube_generation:
            generate_tubes()

        if event.type==periodic_tube_generation2:
            generate_tubes2()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        bird_rect.y -= bird_speed+5
    if bird_rect.y<0:
        bird_rect.y=screen_height
    if bird_rect.y>screen_height:
        bird_rect.y=3

    bird_rect.y += bird_speed

    screen.blit(bg_image,(0,0))
    screen.blit(bird,bird_rect)
    display_tube()
    display_tube2()
    check_collision()
    check_collision2()
    check_points()
    display_scores()
    pygame.display.flip()