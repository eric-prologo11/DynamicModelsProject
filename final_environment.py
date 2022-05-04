# -*- coding: utf-8 -*-
"""
Created on Tue May  3 23:03:43 2022

@author: eprol
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 11:35:05 2022

@author: eprol
"""

import pygame
import numpy as np
import math
import matplotlib.pyplot as plt
#import import_ipynb
import random_walk_checkpoint
import herd_sim

pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255,255,0)
grass = (144, 238, 144)
water = (0, 90, 128)
berries = (150, 0, 150)
food = (0, 100, 0)

dis_width = 800
dis_height = 800

dis = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Predator-Prey Simulation')
 
game_over = False
 
x1 = 400
y1 = 400
 
x1_change = 0       
y1_change = 0

x_axis = []
x = 0
total_herd_mix = []

# Flock variables

N = 103 #No. of Boids
limit = 400 #Axis Limits
limit2 = 450
L  = limit*2
P = 50 #Spread of initial position (gaussian)
V = 50 #Spread of initial velocity (gaussian)
delta = 1 #Time Step
c1 = 0.00001 #Attraction Scaling factor
c2 = 0.01 #Repulsion scaling factor
c3 = 1 #Heading scaling factor
c4 = 0.01 #Randomness scaling factor
vlimit = 2 #Maximum velocity
#Initialize
p = P*np.random.randn(2,N)
v = V*np.random.randn(2,N)

p2 = P*np.random.randn(2,N)
v2 = V*np.random.randn(2,N)

for index in range(len(p[0])):
    if(index >= 51 and index < N):
        temp = p[0][index]
        p[0][index] = p2[0][index]
        p2[0][index] = temp
    
for index in range(len(p[1])):
    if(index >= 51 and index < N):
        temp = p[1][index]
        p[1][index] = p2[1][index]
        p2[1][index] = temp
        
for index in range(len(v[0])):
    if(index >= 51 and index < N):
        temp = v[0][index]
        v[0][index] = v2[0][index]
        v2[0][index] = temp
    
for index in range(len(v[1])):
    if(index >= 51 and index < N):
        temp = v[1][index]
        v[1][index] = v2[1][index]
        v2[1][index] = temp


#top left body of water
p[0][100] = 200
p[1][100] = 100
#right side body of water
p[0][101] = 700
p[1][101] = 100

#top left body of water
p2[0][100] = 200
p2[1][100] = 100
#right side body of water
p2[0][101] = 700
p2[1][101] = 100
"""
#dry season body of water
#right side body of water
p[0][101] = 700
p[1][101] = 100

#top left body of water
p2[0][100] = 700
p2[1][100] = 100
"""
p[0] += limit
p[1] += -limit

p2[0] += limit2
p2[1] += -limit2

buffalo_herd = herd_sim.flock(N,limit,L,P,V,delta,c1,c2,c3,c4,vlimit,p,v)
buffalo_herd_two = herd_sim.flock(N,limit2,L,P,V,delta,c1,c2,c3,c4,vlimit,p2,v2)
# -------
 
clock = pygame.time.Clock()

"""
prevCoord = [p[0][50], p[1][50]]
totalDist = 0
traveledDist = []
"""
 
while not game_over:
    buffalo_herd.p[0][102] = x1
    buffalo_herd.p[1][102] = y1
    buffalo_herd_two.p[0][102] = x1
    buffalo_herd_two.p[1][102] = y1
    buffalo_herd.calc_frame()
    buffalo_herd_two.calc_frame()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if(x1 > 0):
                    #x1 = x1 -10
                    x1_change = -20
                    y1_change = 0
            elif event.key == pygame.K_RIGHT:
                if(x1 < dis_width):
                    #x1 = x1 + 10
                    x1_change = 20
                    y1_change = 0
            elif event.key == pygame.K_UP:
                if(y1_change > -300):
                    #y1 = y1 - 10
                    y1_change = -20
                    x1_change = 0
            elif event.key == pygame.K_DOWN:
                if(y1_change < 300):
                    #y1 = y1 + 10
                    y1_change = 20
                    x1_change = 0
    if (x1 < dis_width and x1 > 0 and y1 < dis_height and y1 > 0) == False:
        x1_change = x1_change*-1
        y1_change = y1_change*-1

    if x1 < dis_width-10 or x1 > 0 or y1 < dis_height-10 or y1 > 0:
        x1 += x1_change
        y1 += y1_change
    
    dis.fill(white)

    #upper left grass
    pygame.draw.ellipse(dis,grass,[-10, -30, 500, 300])
    
    #upper left body of water
    pygame.draw.ellipse(dis,water,[-50, -70, 500, 300])
    
    #right side grass
    pygame.draw.ellipse(dis,grass,[650, 300, 500, 300])

    #right side body of water
    pygame.draw.ellipse(dis,water,[700, 300, 500, 300])
    
    #bottom grass
    pygame.draw.ellipse(dis,grass,[40, 750, 500, 300])
    
    #river for wet season
    pygame.draw.arc(dis,water,[-50, 700, 700, 500], 0, 90)
    """
    
    #bottom grassdry season
    pygame.draw.ellipse(dis,grass,[750, 50, 700, 500])
    
    #river for dry season
    pygame.draw.arc(dis,water,[700, 50, 700, 500], 0, 90)
    
    #river bottom for dry season
    pygame.draw.arc(dis,water,[-50, 700, 700, 500], 0, 90)
    
    #bottom grassdry season
    pygame.draw.ellipse(dis,grass,[40, 750, 500, 300])
    """
    #bottom left patch of food
    #coordinates to input for attraction in random walk:
        #(200, 500), (250, 490), (230, 440), (190, 450), (230, 540)
    #pygame.draw.rect(dis, food, [200, 500, 30, 30])
    #pygame.draw.rect(dis, food, [250, 490, 30, 30])
    #pygame.draw.rect(dis, food, [230, 440, 30, 30])
    #pygame.draw.rect(dis, berries, [190, 450, 30, 30])
    #pygame.draw.rect(dis, berries, [230, 540, 30, 30])

    #lower right patch of food
    #coordinates to input for attraction in random walk:
        #(600, 100), (650, 90), (630, 40), (590, 50), (630, 140)
    #pygame.draw.rect(dis, food, [600, 100, 30, 30])
    #pygame.draw.rect(dis, food, [650, 90, 30, 30])
    #pygame.draw.rect(dis, food, [630, 40, 30, 30])
    #pygame.draw.rect(dis, berries, [590, 50, 30, 30])
    #pygame.draw.rect(dis, berries, [630, 140, 30, 30])


    pygame.draw.rect(dis, orange, [x1, y1, 10, 10])
    
    #print("drawing water")
    counter = 0
    for i in range(0,len(p[0])-2):
        if(counter%10 != 0):
            pygame.draw.circle(dis,black,(buffalo_herd.p[0,i],buffalo_herd.p[1,i]),2)
            pygame.draw.circle(dis,black,(buffalo_herd_two.p[0,i],buffalo_herd_two.p[1,i]),2)
        else:
            pygame.draw.circle(dis,yellow,(buffalo_herd.p[0,i],buffalo_herd.p[1,i]),2)
            pygame.draw.circle(dis,yellow,(buffalo_herd_two.p[0,i],buffalo_herd_two.p[1,i]),2)
        counter = counter + 1
        #pygame.draw.quiver(dis,black,(buffalo_herd.p[0,i],buffalo_herd.p[1,i]),2)

    #print("done printing water")

    pygame.display.update()
    """
    herd_switch_array= []
    totalDist = 0
    for index in range(50, len(p[0])-2):
        pCoord = [p[0][index], p[1][index]]
        p2Coord = [p2[0][index], p2[1][index]]
        totalDist += math.sqrt((pCoord[0]-p2Coord[0])**2 + (pCoord[1] - p2Coord[1])**2)
        if(totalDist < 1000):
            herd_switch_array.append(totalDist)
    print(herd_switch_array)
    total_herd_mix.append(len(herd_switch_array))
    x_axis.append(x)
    x += 1
    
    plt.plot(x_axis, total_herd_mix)
    plt.title("water buffalo agent herd switching")
    plt.xlabel("time steps (30 clock cycle)")
    plt.ylabel("total amount of agents mixed between herds")
    plt.show()
    
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    langs = ['Wet', 'Dry']
    distance = [170.55, 399.19]
    ax.bar(langs, distance)
    plt.show()

    index = 0
    density_array = []
    x_axis = 0
    x_axis_array = []
    while(index < dis_width):
        counter = 0
        j = 0
        while(j < dis_height):
            for coord in range(len(p[0])):
                if((p[0][coord] >= index) and (p[0][coord] < index + 20) and (p[1][coord] >= j) and (p[1][coord] < j + 20)):
                    counter += 1
            density_array.append(counter)
            x_axis_array.append(x_axis)
            x_axis += 1
            j += 20
        index += 20
        
    plt.plot(x_axis_array, density_array)
    plt.title("water buffalo density in 400 square grid spaces")
    plt.xlabel("each of the 400 square unit grid spaces")
    plt.ylabel("amount of water buffalo (per 400 square grid spaces)")
    plt.show()
    """
    
    clock.tick(30)
    
pygame.quit()
quit()


