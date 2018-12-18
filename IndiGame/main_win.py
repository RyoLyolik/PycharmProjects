# TRAINING


import pygame
import random
import math
pygame.init()

size = w, h = 720, 480
speed = [random.choice(range(1, 5)), random.choice(range(1, 5))]  # x speed , y speed
speed_1 = [random.choice(range(1, 5)), random.choice(range(1, 5))]
speed_2 = [random.choice(range(1, 5)), random.choice(range(1, 5))]
speed_3 = [random.choice(range(1, 5)), random.choice(range(1, 5))]

screen = pygame.display.set_mode(size)

ball = pygame.image.load("temporily_ball.png")
ball_size = 64
ballrect = pygame.draw.rect(screen, (200, 100, 150), (190, 60, ball_size, ball_size), 0)
ballrect_1 = pygame.draw.rect(screen, (200, 100, 150), (20, 20, ball_size, ball_size), 0)
ballrect_2 = pygame.draw.rect(screen, (200, 100, 150), (300, 290, ball_size, ball_size), 0)
ballrect_3 = pygame.draw.rect(screen, (200, 100, 150), (300, 290, ball_size, ball_size), 0)
bot_ch = False
top_ch = False
left_ch = False
right_ch = False

bot_ch_1 = False
top_ch_1 = False
left_ch_1 = False
right_ch_1 = False

bot_ch_2 = False
top_ch_2 = False
left_ch_2 = False
right_ch_2 = False

bot_ch_3 = False
top_ch_3 = False
left_ch_3 = False
right_ch_3 = False
flipping = True
tmr = 0
pos = pygame.mouse.get_pos()
player = pygame.draw.rect(screen, (200, 100, 150), (pos[0], pos[1], 10, 10), 0)


def game_over():
    global ballrect, ballrect_1, ballrect_2, player, flipping
    if (player.left <= ballrect.right) and (
            player.left - ballrect.right <= ball_size) and (
            player.top < ballrect.bottom and player.bottom > ballrect.top) and (player.right >= ballrect.left) and (
            player.right - ballrect.right <= ball_size):
        if flipping:
            print('game_over')
            flipping = False

    if (player.left <= ballrect_1.right) and (
            player.left - ballrect_1.right <= ball_size) and (
            player.top < ballrect_1.bottom and player.bottom > ballrect_1.top) and (
            player.right >= ballrect_1.left) and (
            player.right - ballrect_1.right <= ball_size):
        if flipping:
            print('game_over')
            flipping = False

    if (player.left <= ballrect_2.right) and (
            player.left - ballrect_2.right <= ball_size) and (
            player.top < ballrect_2.bottom and player.bottom > ballrect_2.top) and (
            player.right >= ballrect_2.left) and (
            player.right - ballrect_2.right <= ball_size):
        if flipping:
            print('game_over')
            flipping = False

    if (player.left <= ballrect_3.right) and (
            player.left - ballrect_3.right <= ball_size) and (
            player.top < ballrect_3.bottom and player.bottom > ballrect_3.top) and (
            player.right >= ballrect_3.left) and (
            player.right - ballrect_3.right <= ball_size):
        if flipping:
            print('game_over')
            flipping = False

    # if (player.top <= ballrect.bottom or player.top <= ballrect_1.bottom or player.top <= ballrect_2.bottom) and (player.top - ballrect.bottom >= ball_size or player.top - ballrect_1.bottom >= ball_size or player.top - ballrect_2.bottom >= ball_size):
    #     if flipping:
    #         print('game_over')
    #     flipping = False


def checking():
    global ballrect, speed, speed_1, speed_2, speed_3, bot_ch, top_ch, left_ch, right_ch, ballrect_1, ballrect_2, ballrect_3, bot_ch_1, top_ch_1, left_ch_1, right_ch_1, bot_ch_2, top_ch_2, left_ch_2, right_ch_2, tmr, player, bot_ch_3, top_ch_3, left_ch_3, right_ch_3
    if ballrect.left <= 10 and left_ch == False:
        right_ch = False
        left_ch = True
        speed[0] = -speed[0]
        # if speed[0] < 0:
        #     speed[0] += speed[0] / k
        # else:
        #     speed[0] -= speed[0] / k
    if ballrect.right - w > -10 and right_ch == False:
        left_ch = False
        right_ch = True
        speed[0] = -speed[0]
        # if speed[0] < 0:
        #     speed[0] -= speed[0] / k
        # else:
        #     speed[0] += speed[0] / k
    elif ballrect.bottom - h > -10 and bot_ch == False:
        bot_ch = True
        top_ch = False
        speed[1] = -(speed[1])
        # if speed[1] < 0:
        #     speed[1] -= speed[1] / k
        # else:
        #     speed[1] += speed[1] / k
    if ballrect.top <= 10 and top_ch == False:
        bot_ch = False
        top_ch = True
        speed[1] = -(speed[1])

        if ballrect.left <= 10 and left_ch == False:
            right_ch = False
            left_ch = True
            speed[0] = -speed[0]
            # if speed[0] < 0:
            #     speed[0] += speed[0] / k
            # else:
            #     speed[0] -= speed[0] / k
        if ballrect.right - w > -10 and right_ch == False:
            left_ch = False
            right_ch = True
            speed[0] = -speed[0]
            # if speed[0] < 0:
            #     speed[0] -= speed[0] / k
            # else:
            #     speed[0] += speed[0] / k
        elif ballrect.bottom - h > -10 and bot_ch == False:
            bot_ch = True
            top_ch = False
            speed[1] = -(speed[1])
            # if speed[1] < 0:
            #     speed[1] -= speed[1] / k
            # else:
            #     speed[1] += speed[1] / k
        if ballrect.top <= 10 and top_ch == False:
            bot_ch = False
            top_ch = True
            speed[1] = -(speed[1])

        # if speed[1] < 0:
        #     speed[1] += speed[1] / k
        # else:
        #     speed[1] -= speed[1] / k

    if ballrect_1.left <= 10 and left_ch_1 == False:
        right_ch_1 = False
        left_ch_1 = True
        speed_1[0] = -speed_1[0]
        # if speed[0] < 0:
        #     speed[0] += speed[0] / k
        # else:
        #     speed[0] -= speed[0] / k
    if ballrect_1.right - w > -10 and right_ch_1 == False:
        left_ch_1 = False
        right_ch_1 = True
        speed_1[0] = -speed_1[0]
        # if speed[0] < 0:
        #     speed[0] -= speed[0] / k
        # else:
        #     speed[0] += speed[0] / k
    elif ballrect_1.bottom - h > -10 and bot_ch_1 == False:
        bot_ch_1 = True
        top_ch_1 = False
        speed_1[1] = -(speed_1[1])
        # if speed[1] < 0:
        #     speed[1] -= speed[1] / k
        # else:
        #     speed[1] += speed[1] / k
    if ballrect_1.top <= 10 and top_ch_1 == False:
        bot_ch_1 = False
        top_ch_1 = True
        speed_1[1] = -(speed_1[1])

    if ballrect_2.left <= 10 and left_ch_2 == False:
        right_ch_2 = False
        left_ch_2 = True
        speed_2[0] = -speed_2[0]
        # if speed[0] < 0:
        #     speed[0] += speed[0] / k
        # else:
        #     speed[0] -= speed[0] / k
    if ballrect_2.right - w > -10 and right_ch_2 == False:
        left_ch_2 = False
        right_ch_2 = True
        speed_2[0] = -speed_2[0]
        # if speed[0] < 0:
        #     speed[0] -= speed[0] / k
        # else:
        #     speed[0] += speed[0] / k
    elif ballrect_2.bottom - h > -10 and bot_ch_2 == False:
        bot_ch_2 = True
        top_ch_2 = False
        speed_2[1] = -(speed_2[1])
        # if speed[1] < 0:
        #     speed[1] -= speed[1] / k
        # else:
        #     speed[1] += speed[1] / k
    if ballrect_2.top <= 10 and top_ch_2 == False:
        bot_ch_2 = False
        top_ch_2 = True
        speed_2[1] = -(speed_2[1])

    ####

    if ballrect_3.left <= 10 and left_ch_3 == False:
        right_ch_3 = False
        left_ch_3 = True
        speed_3[0] = -speed_3[0]
        # if speed[0] < 0:
        #     speed[0] += speed[0] / k
        # else:
        #     speed[0] -= speed[0] / k
    if ballrect_3.right - w > -10 and right_ch_3 == False:
        left_ch_3 = False
        right_ch_3 = True
        speed_3[0] = -speed_3[0]
        # if speed[0] < 0:
        #     speed[0] -= speed[0] / k
        # else:
        #     speed[0] += speed[0] / k
    elif ballrect_3.bottom - h > -10 and bot_ch_3 == False:
        bot_ch_3 = True
        top_ch_3 = False
        speed_3[1] = -(speed_3[1])
        # if speed[1] < 0:
        #     speed[1] -= speed[1] / k
        # else:
        #     speed[1] += speed[1] / k
    if ballrect_3.top <= 10 and top_ch_3 == False:
        bot_ch_3 = False
        top_ch_3 = True
        speed_3[1] = -(speed_3[1])

def draw_ball():
    global ballrect, speed, speed_1, speed_2, speed_3, bot_ch, top_ch, left_ch, right_ch, ballrect_1, ballrect_2, ballrect_3, bot_ch_1, top_ch_1, left_ch_1, right_ch_1, bot_ch_2, top_ch_2, left_ch_2, right_ch_2, tmr, player, bot_ch_3, top_ch_3, left_ch_3, right_ch_3
    game_over()
    pos = pygame.mouse.get_pos()
    k = 5
    screen.fill((0, 0, 0))
    ballrect = ballrect.move(speed) # move x+2 y+2 for one step
    ballrect_1 = ballrect_1.move(speed_1)
    ballrect_2 = ballrect_2.move(speed_2)
    ballrect_3 = ballrect_3.move(speed_3)

    ballrect = pygame.draw.rect(screen, (200, 100, 150), (ballrect.left, ballrect.top, ball_size, ball_size), 0)
    ballrect_1 = pygame.draw.rect(screen, (200, 100, 150), (ballrect_1.left, ballrect_1.top, ball_size, ball_size), 0)
    ballrect_2 = pygame.draw.rect(screen, (200, 100, 150), (ballrect_2.left, ballrect_2.top, ball_size, ball_size), 0)
    ballrect_3 = pygame.draw.rect(screen, (200, 100, 150), (ballrect_3.left, ballrect_3.top, ball_size, ball_size), 0)

    player = pygame.draw.rect(screen, (100, 200, 150), (pos[0], pos[1], 10, 10), 0)
    # print(speed,speed1)
    if tmr >= random.choice(range(100, 500)):
        # speed = [random.choice(range(1, 5)), random.choice(range(1, 5))]  # x speed , y speed
        # speed_1 = [random.choice(range(1, 5)), random.choice(range(1, 5))]
        # speed_2 = [random.choice(range(1, 5)), random.choice(range(1, 5))]
        speed = [-i for i in speed]
        speed_1 = [-i for i in speed_1]
        speed_2 = [-i for i in speed_2]
        checking()
        tmr = 0
    else:
        checking()


while pygame.event.wait().type != pygame.QUIT:
    # tmr += random.random()
    draw_ball()
    if flipping:
        pygame.display.flip()

pygame.quit()