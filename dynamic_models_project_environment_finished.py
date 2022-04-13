import pygame
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
water = (0, 90, 128)
berries = (150, 0, 150)
food = (0, 100, 0)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game by Edureka')
 
game_over = False
 
x1 = 300
y1 = 300
 
x1_change = 0       
y1_change = 0
 
clock = pygame.time.Clock()
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if(x1 > 0):
                    #x1 = x1 -10
                    x1_change = -5
                    y1_change = 0
            elif event.key == pygame.K_RIGHT:
                if(x1 < dis_width):
                    #x1 = x1 + 10
                    x1_change = 5
                    y1_change = 0
            elif event.key == pygame.K_UP:
                if(y1_change > -300):
                    #y1 = y1 - 10
                    y1_change = -5
                    x1_change = 0
            elif event.key == pygame.K_DOWN:
                if(y1_change < 300):
                    #y1 = y1 + 10
                    y1_change = 5
                    x1_change = 0
 
    if x1 < dis_width or x1 > 0 or y1 < dis_height or y1 > 0:
        x1 += x1_change
        y1 += y1_change
    dis.fill(white)
    #upper left body of water
    #coordinates to input for attraction in random walk: 
        #(310, 0), (320, 0), (330, 0), (340, 0), (350, 0), (270, 20), (240, 40), 
        #(210, 60), (180, 80), (150, 100), (120, 120), (0, 140), (60, 160), (30, 180), (0, 200)
    pygame.draw.rect(dis, water, [0, 0, 30, 30])
    
    pygame.draw.rect(dis, water, [30, 0, 30, 30])
    pygame.draw.rect(dis, water, [60, 0, 30, 30])
    pygame.draw.rect(dis, water, [90, 0, 30, 30])
    pygame.draw.rect(dis, water, [120, 0, 30, 30])
    pygame.draw.rect(dis, water, [150, 0, 30, 30])
    pygame.draw.rect(dis, water, [180, 0, 30, 30])
    pygame.draw.rect(dis, water, [210, 0, 30, 30])
    pygame.draw.rect(dis, water, [240, 0, 30, 30])
    pygame.draw.rect(dis, water, [270, 0, 30, 30])
    pygame.draw.rect(dis, water, [300, 0, 30, 30])
    pygame.draw.rect(dis, water, [310, -5, 30, 30])
    pygame.draw.rect(dis, water, [320, -10, 30, 30])
    pygame.draw.rect(dis, water, [330, -15, 30, 30])
    pygame.draw.rect(dis, water, [340, -20, 30, 30])
    pygame.draw.rect(dis, water, [350, -25, 30, 30])
    
    pygame.draw.rect(dis, water, [0, 30, 30, 30])
    pygame.draw.rect(dis, water, [0, 60, 30, 30])
    pygame.draw.rect(dis, water, [0, 90, 30, 30])
    pygame.draw.rect(dis, water, [0, 120, 30, 30])
    
    pygame.draw.rect(dis, water, [20, 20, 30, 30])
    pygame.draw.rect(dis, water, [30, 20, 30, 30])
    pygame.draw.rect(dis, water, [60, 20, 30, 30])
    pygame.draw.rect(dis, water, [90, 20, 30, 30])
    pygame.draw.rect(dis, water, [120, 20, 30, 30])
    pygame.draw.rect(dis, water, [150, 20, 30, 30])
    pygame.draw.rect(dis, water, [180, 20, 30, 30])
    pygame.draw.rect(dis, water, [210, 20, 30, 30])
    pygame.draw.rect(dis, water, [240, 20, 30, 30])
    pygame.draw.rect(dis, water, [270, 20, 30, 30])

    pygame.draw.rect(dis, water, [40, 40, 30, 30])
    pygame.draw.rect(dis, water, [30, 40, 30, 30])
    pygame.draw.rect(dis, water, [60, 40, 30, 30])
    pygame.draw.rect(dis, water, [90, 40, 30, 30])
    pygame.draw.rect(dis, water, [120, 40, 30, 30])
    pygame.draw.rect(dis, water, [150, 40, 30, 30])
    pygame.draw.rect(dis, water, [180, 40, 30, 30])
    pygame.draw.rect(dis, water, [210, 40, 30, 30])
    pygame.draw.rect(dis, water, [240, 40, 30, 30])
    
    pygame.draw.rect(dis, water, [60, 60, 30, 30])
    pygame.draw.rect(dis, water, [30, 60, 30, 30])
    pygame.draw.rect(dis, water, [60, 60, 30, 30])
    pygame.draw.rect(dis, water, [90, 60, 30, 30])
    pygame.draw.rect(dis, water, [120, 60, 30, 30])
    pygame.draw.rect(dis, water, [150, 60, 30, 30])
    pygame.draw.rect(dis, water, [180, 60, 30, 30])
    pygame.draw.rect(dis, water, [210, 60, 30, 30])
    
    pygame.draw.rect(dis, water, [80, 80, 30, 30])
    pygame.draw.rect(dis, water, [30, 80, 30, 30])
    pygame.draw.rect(dis, water, [60, 80, 30, 30])
    pygame.draw.rect(dis, water, [90, 80, 30, 30])
    pygame.draw.rect(dis, water, [120, 80, 30, 30])
    pygame.draw.rect(dis, water, [150, 80, 30, 30])
    pygame.draw.rect(dis, water, [180, 80, 30, 30])
    
    pygame.draw.rect(dis, water, [100, 100, 30, 30])
    pygame.draw.rect(dis, water, [30, 100, 30, 30])
    pygame.draw.rect(dis, water, [60, 100, 30, 30])
    pygame.draw.rect(dis, water, [90, 100, 30, 30])
    pygame.draw.rect(dis, water, [120, 100, 30, 30])
    pygame.draw.rect(dis, water, [150, 100, 30, 30])
    
    pygame.draw.rect(dis, water, [120, 120, 30, 30])
    pygame.draw.rect(dis, water, [30, 120, 30, 30])
    pygame.draw.rect(dis, water, [60, 120, 30, 30])
    pygame.draw.rect(dis, water, [90, 120, 30, 30])
    pygame.draw.rect(dis, water, [120, 120, 30, 30])
    
    pygame.draw.rect(dis, water, [30, 140, 30, 30])
    pygame.draw.rect(dis, water, [60, 140, 30, 30])
    pygame.draw.rect(dis, water, [90, 140, 30, 30])
    pygame.draw.rect(dis, water, [0, 140, 30, 30])
    
    pygame.draw.rect(dis, water, [0, 160, 30, 30])
    pygame.draw.rect(dis, water, [30, 160, 30, 30])
    pygame.draw.rect(dis, water, [60, 160, 30, 30])
    
    pygame.draw.rect(dis, water, [0, 180, 30, 30])
    pygame.draw.rect(dis, water, [30, 180, 30, 30])
    
    pygame.draw.rect(dis, water, [0, 200, 30, 30])
    
    #right side body of water
    #coordinates to input for attraction in random walk:
        #(700, 300), (720, 280), (740, 260), (760, 240), (780, 220), (720, 320),
        #(740, 340), (760, 360), (780, 380)
    pygame.draw.rect(dis, water, [700, 300, 30, 30])
    pygame.draw.rect(dis, water, [730, 300, 30, 30])
    pygame.draw.rect(dis, water, [760, 300, 30, 30])
    pygame.draw.rect(dis, water, [790, 300, 30, 30])
    
    pygame.draw.rect(dis, water, [730, 280, 30, 30])
    pygame.draw.rect(dis, water, [760, 280, 30, 30])
    pygame.draw.rect(dis, water, [790, 280, 30, 30])
    pygame.draw.rect(dis, water, [760, 260, 30, 30])
    pygame.draw.rect(dis, water, [790, 260, 30, 30])
    pygame.draw.rect(dis, water, [790, 240, 30, 30])
    
    pygame.draw.rect(dis, water, [730, 320, 30, 30])
    pygame.draw.rect(dis, water, [760, 320, 30, 30])
    pygame.draw.rect(dis, water, [790, 320, 30, 30])
    pygame.draw.rect(dis, water, [760, 340, 30, 30])
    pygame.draw.rect(dis, water, [790, 340, 30, 30])
    pygame.draw.rect(dis, water, [790, 360, 30, 30])
    
    pygame.draw.rect(dis, water, [720, 280, 30, 30])
    pygame.draw.rect(dis, water, [740, 260, 30, 30])
    pygame.draw.rect(dis, water, [760, 240, 30, 30])
    pygame.draw.rect(dis, water, [780, 220, 30, 30])
    
    pygame.draw.rect(dis, water, [720, 320, 30, 30])
    pygame.draw.rect(dis, water, [740, 340, 30, 30])
    pygame.draw.rect(dis, water, [760, 360, 30, 30])
    pygame.draw.rect(dis, water, [780, 380, 30, 30])
    
    #bottom left patch of food
    #coordinates to input for attraction in random walk:
        #(200, 500), (250, 490), (230, 440), (190, 450), (230, 540)
    pygame.draw.rect(dis, food, [200, 500, 30, 30])
    pygame.draw.rect(dis, food, [250, 490, 30, 30])
    pygame.draw.rect(dis, food, [230, 440, 30, 30])
    pygame.draw.rect(dis, berries, [190, 450, 30, 30])
    pygame.draw.rect(dis, berries, [230, 540, 30, 30])
    
    #lower right patch of food
    #coordinates to input for attraction in random walk:
        #(600, 100), (650, 90), (630, 40), (590, 50), (630, 140)
    pygame.draw.rect(dis, food, [600, 100, 30, 30])
    pygame.draw.rect(dis, food, [650, 90, 30, 30])
    pygame.draw.rect(dis, food, [630, 40, 30, 30])
    pygame.draw.rect(dis, berries, [590, 50, 30, 30])
    pygame.draw.rect(dis, berries, [630, 140, 30, 30])
    
    
    pygame.draw.rect(dis, orange, [x1, y1, 10, 10])
    
 
    pygame.display.update()
 
    clock.tick(30)
 
pygame.quit()
quit()