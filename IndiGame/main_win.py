import pygame
import random
import math
pygame.init()

size = w, h = 720, 480
speed = [random.choice(range(1,100)),random.choice(range(1,100))] # x speed , y speed

screen = pygame.display.set_mode(size)

ball = pygame.image.load("temporily_ball.png")
ball_size = 64
ballrect = pygame.draw.rect(screen,(200,100,150), (20,20, ball_size, ball_size), 0)
bot_ch = False
top_ch = False
left_ch = False
right_ch = False
def draw_ball():
    global ballrect, speed, bot_ch, top_ch, left_ch, right_ch

    ballrect = ballrect.move(speed) # move x+2 y+2 for one step

    screen.fill((0,0,0))
    ballrect = pygame.draw.rect(screen, (200, 100, 150), (ballrect.left, ballrect.top, ball_size, ball_size), 0)
    if ballrect.left <= 10 and left_ch == False:
        right_ch = False
        left_ch = True
        speed[0] = -speed[0]
        if speed[0] < 0:
            speed[0] -= speed[0] / 10
        else:
            speed[0] += speed[0] / 10
    if ballrect.right - w > -10 and right_ch == False:
        left_ch = False
        right_ch = True
        speed[0] = -speed[0]
        if speed[0] < 0:
            speed[0] -= speed[0] / 10
        else:
            speed[0] += speed[0] / 10
    elif ballrect.bottom - h > -10 and bot_ch == False:
        bot_ch = True
        top_ch = False
        speed[1] = -(speed[1])
        if speed[1] < 0:
            speed[1] -= speed[1] / 10
        else:
            speed[1] += speed[1] / 10
    if ballrect.top <= 10 and top_ch == False:
        bot_ch = False
        top_ch = True
        speed[1] = -(speed[1])

        if speed[1] < 0:
            speed[1] -= speed[1] / 10
        else:
            speed[1] += speed[1] / 10

    print(ballrect.top < 0)
    print(speed)
    pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    draw_ball()


pygame.quit()