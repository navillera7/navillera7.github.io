import pygame
import math
import time

import serial


r1 = 24.813
r2 = 25.038
def isnegative (a):
    if a < 0:
        return "n"
    else:
        return "p"
def rtod (a):
    return a * 180 / math.pi

def angle1 (x, z):
    return rtod(math.atan(x/z))

def dis(x, y, z):
    return math.sqrt(pow(x, 2) + pow(y, 2) + pow(z, 2))

def angle3 (x, y, z):
    return rtod(math.acos((pow(dis(x, y, z), 2) - pow(r1, 2) - pow(r2, 2))/ (-2 * r1 * r2)))

def angle2 (x, y, z):
    return rtod(math.asin(math.sin(angle3(x, y, z) * r2 / dis(x, y, z))) + math.acos(math.sqrt(pow(x, 2) + pow(z, 2)) / dis(x, y, z)))

def ctod (x, y, z, w):
    if w == 0:
        if x == 0: 
            return 0
        else:
            return math.atan(z/x)
    elif w==1:
        return angle2(x,y,z)
    elif w==2:
        return angle3(x, y, z)

pygame.init() 
 
img = pygame.image.load('arr.png')
img = pygame.transform.scale(img, (50, 50))
WHITE = (255,255,255)
size = [800, 800]
screen = pygame.display.set_mode(size)
 
done= False
clock= pygame.time.Clock()

BLACK = (0,0,0)
RED = (255, 0, 0)
GREY = (150, 150, 150)
GG = [BLACK, BLACK, BLACK, BLACK, BLACK, BLACK, BLACK]


smallfont = pygame.font.SysFont('Corbel', 35)
smallfont2 = pygame.font.SysFont('Corbel', 20)
smallfont3 = pygame.font.SysFont('Corbel', 15)
smallfont4 = pygame.font.SysFont('Corbel', 55)

def confirmed (a):
    return smallfont.render(a, True, (255, 255, 255))
def confirmed2 (a):
    return smallfont2.render(a, True, (255, 255, 255))
def confirmed3 (a):
    return smallfont2.render(a, True, (0, 0, 0))

def confirmed4 (a):
    return smallfont3.render(a, True, (0, 0, 0))

def confirmed5 (a):
    return smallfont4.render(a, True, (255, 255, 255))

def runGame():
    
    global done
    x = 0
    y = 0
    z = 10
    a = 0
    b = 0
    c = 0
    r = 40
    n = 10
    x1 = 500
    draw = 0
    temp1 = 90
    temp2 = 90
    temp3 = 90
    drawing = []

    while not done:
        clock.tick(5)
        mouse = pygame.mouse.get_pos()

 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done=True
 
            # 방향키 입력에 대한 이벤트 처리
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and y0 > 80:
                    y -= 15
                    GG[0] = GREY
                    temp1 = ctod(xn, yn, z0, 0)
                    temp2 = ctod(xn, yn, z0, 1)
                    temp3 = ctod(xn, yn, z0, 2)
                    draw = 1

                elif event.key == pygame.K_s and y0 < 340:
                    y += 15
                    GG[4] = GREY
                    temp1 = ctod(xn, yn, z0, 0)
                    temp2 = ctod(xn, yn, z0, 1)
                    temp3 = ctod(xn, yn, z0, 2)
                    draw = 1
                elif event.key == pygame.K_a and x0 > 130:
                    x -= 10
                    GG[2] = GREY
                    temp1 = ctod(xn, yn, z0, 0)
                    temp2 = ctod(xn, yn, z0, 1)
                    temp3 = ctod(xn, yn, z0, 2)
                    draw = 1 
                elif event.key == pygame.K_d and x0 < 670:
                    x += 10
                    GG[3] = GREY
                    temp1 = ctod(xn, yn, z0, 0)
                    temp2 = ctod(xn, yn, z0, 1)
                    temp3 = ctod(xn, yn, z0, 2)
                    draw = 1
                elif event.key == pygame.K_q and z < 20:
                    z += 1
                    GG[1] = GREY
                    temp1 = ctod(xn, yn, z0, 0)
                    temp2 = ctod(xn, yn, z0, 1)
                    temp3 = ctod(xn, yn, z0, 2)
                    draw = 1 
                elif event.key == pygame.K_e and z > 10:
                    z -= 1
                    GG[5] = GREY
                    temp1 = ctod(xn, yn, z0, 0)
                    temp2 = ctod(xn, yn, z0, 1)
                    temp3 = ctod(xn, yn, z0, 2)
                    draw = 1
                elif event.key == pygame.K_p:
                    GG[6] = GREY
                    drawing.append([x0, y0])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 580<= mouse[0] <= 630 and 430 <= mouse[1] <= 470:
                    a = a + 1
                if 580<= mouse[0] <= 630 and 530 <= mouse[1] <= 570:
                    b = b + 1
                if 580<= mouse[0] <= 630 and 680 <= mouse[1] <= 720:
                    c = c + 1
                if 500<= mouse[0] <= 700 and 600 <= mouse[1] <= 610:
                    r = abs((500 - mouse[0])/2)
                    x1 = mouse[0]
        
        
        screen.fill(WHITE)
        pygame.draw.rect(screen,BLACK,(100,60,600,310))
        pygame.draw.rect(screen,GG[0],(100,400,50,50))
        pygame.draw.rect(screen,GG[1],(220,400,50,50))
        pygame.draw.rect(screen,GG[2],(40,460,50,50))
        pygame.draw.rect(screen,GG[3],(160,460,50,50))
        pygame.draw.rect(screen,GG[4],(100,520,50,50))
        pygame.draw.rect(screen,GG[5],(220,460,50,50))
        pygame.draw.rect(screen,GG[6],(220,560,50,50))
        for i in range (0, 7):
            GG[i] = BLACK
        pygame.display.set_caption("Control interface")

        screen.blit(confirmed("W"), (110, 410))
        screen.blit(confirmed("Q"), (230, 410))
        screen.blit(confirmed("E"), (230, 470))
        screen.blit(confirmed("P"), (230, 570))
        screen.blit(confirmed("D"), (172, 470))
        screen.blit(confirmed("A"), (53, 470))
        screen.blit(confirmed("S"), (110, 530))
        screen.blit(confirmed4("0%"), (490, 615))
        screen.blit(confirmed4("100%"), (690, 615))
        
        for i in drawing:
            pygame.draw.circle(screen, (0, 0, 200), (i[0], i[1]), 25)
        
        screen.blit(img, (100, 460))

        screen.blit(confirmed2("CAMERA SCREEN"), (110, 75))
        screen.blit(confirmed3("FLASH LIGHT"), (550, 500))

        pygame.draw.circle(screen,(200, 0, 0), (600, 450), 20)

        pygame.draw.rect(screen,(0, 0,0),(500,600,200,6))
        pygame.draw.circle(screen,(100, 100, 100), (x1, 603), 12)
        screen.blit(confirmed3("EMERGENCY STOP"), (522, 405))



        screen.blit(confirmed3("AUTO MODE"), (550, 650))

        if a%2 == 0:
            pygame.draw.circle(screen,(200, 0, 0), (600, 450), 20)
            x0 = 400+x
            y0 = 200 + y
            z0 = z
        else:
            pygame.draw.circle(screen,(30, 100, 30), (600, 450), 20)
            screen.blit(confirmed5("PAUSED"), (300, 90))
            c = 0
            
        if b%2 == 0:
            pygame.draw.circle(screen,(0, 0, 0), (600, 550), 20)
            screen.blit(confirmed2("OFF"), (582, 540))
        else:
            pygame.draw.circle(screen,(255, 200, 0), (600, 550), 20)
            screen.blit(confirmed3("ON"), (585, 540))
            pygame.draw.circle(screen,(255, 255, 0), (x0, y0), r*2/3)

        if c%2 == 0:
            
            pygame.draw.circle(screen,(0, 0, 0), (600, 700), 20)
            screen.blit(confirmed2("OFF"), (582, 690))
            t = 0
        else:
            if t == 0:
                x = -250
                y = 140
            
            if 140 <= x0 <= 670 and 80 <= y0 <= 340: 
                x = x + n 
                if t == 0:
                    pass
                else:
                    drawing.append([x0, y0])
                print(x0)
        
            if x0 == 660:
                y = y - 20
                n =  -10
                drawing.append([x0, y0])
            if x0 == 150:
                y = y - 20
                n = 10
                drawing.append([x0, y0])
            t = t + 1
                
            
            pygame.draw.circle(screen,(255, 200, 0), (600, 700), 20)
            screen.blit(confirmed3("ON"), (585, 690))


        xn = (x0-400)/10
        yn = (y0-500)/-15
        
        d1 = (temp1 - ctod(xn, yn, z0, 0)) 
        d2 = (temp2 - ctod(xn, yn, z0, 1)) 
        d3 = (temp3 - ctod(xn, yn, z0, 2))

        screen.blit(confirmed3("COORDINATES"), (300, 400))
        screen.blit(confirmed3("X: "), (300, 430))
        screen.blit(confirmed3(str(xn)), (320, 430))
        screen.blit(confirmed3("Y: "), (300, 460))
        screen.blit(confirmed3(str(round(yn, 1))), (320, 460))
        screen.blit(confirmed3("Z: "), (300, 490))
        screen.blit(confirmed3(str(z0)), (320, 490))
        screen.blit(confirmed3("Difference of ANGLES"), (300, 520))
        screen.blit(confirmed3("φ: "), (300, 550))
        screen.blit(confirmed3(str(round(d1, 2))), (320, 550))
        screen.blit(confirmed3("θ: "), (300, 580))
        screen.blit(confirmed3(str(round(d2, 2))), (320, 580))
        screen.blit(confirmed3("ψ: "), (300, 610))
        screen.blit(confirmed3(str(round(d3, 2))), (320, 610))
        #pygame.draw.rect(screen,BLACK,(100,70,600,300))
        pygame.draw.rect(screen, (255, 255, 255), (700, 70, 100, 500))
        pygame.draw.rect(screen, (255, 255, 255), (0, 70, 100, 370))
        pygame.draw.rect(screen, (255, 255, 255), (100, 370, 600, 30))
        pygame.draw.rect(screen, (255, 255, 255), (0, 0, 1000, 70))
        
        pygame.draw.rect(screen,RED,(x0-2,y0-13,4,30))
        pygame.draw.rect(screen,RED,(x0-15,y0,30,4))
        screen.blit(confirmed2("CAMERA SCREEN"), (110, 75))
        screen.blit(confirmed4("Front"), (220, 385))
        screen.blit(confirmed4("Back"), (220, 510))
        pygame.display.update()

        # ARDUINO
        # if draw == 1:
        #     port = "COM8"
        #     bdrate = 115200 
        #     ard = serial.Serial(port, bdrate)

        #     ard.close()

        #     ard = serial.Serial(port, bdrate)

        #     val = isnegative(d1) + str(d1) + isnegative(d2) + str(d2) + isnegative(d3) + str(d3)
            
        #     val = val.encode('utf-8')
            
        #     ard.write(val)

        #     ard.close()
        # draw = 0

        
 
runGame()
pygame.quit()
