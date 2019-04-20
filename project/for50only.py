import random
import pygame
pygame.init()

#resolution of display
height_disp=925
width_disp=1050

gameDisplay=pygame.display.set_mode((width_disp,height_disp))
pygame.display.set_caption("TETRIS")
clock=pygame.time.Clock()

figure_step=100
point=0
score=0
y_base=[height_disp for i in range(10)]

#height_current=height_figure
j=1

x=525
y=25
width_figure=100
height_figure=100

figures_on_disp =[[0,0,0,0]] # list of figure`s parametrs on display


WHITE = (255, 255, 255)  
ORANGE = (255, 150, 100)
BLACK = (0,0,0)

done = False
# -------- Main Program Loop -----------
while not done:
  # --- Main event loop
    pygame.time.delay(400)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x>figure_step:
            x=x-figure_step
    if keys[pygame.K_RIGHT] and x<(width_disp-width_figure-figure_step):
            x=x+figure_step
    if keys[pygame.K_UP] and y>figure_step:
            y=y-figure_step
    if keys[pygame.K_DOWN] and y<(height_disp - height_figure-figure_step):
            y=y+figure_step
    
   
   

    gameDisplay.fill((0,0,0))

    # moving figure to down
    
    if y<=(height_disp-height_figure-figure_step):
        y+=figure_step
    #------------------------------------------------------------------------
    for i in range(10):
        if x==(i*100+25):
            if (y+height_figure==y_base[i]):
                figures_on_disp.append([x,y,width_figure,height_figure])
                y_base[i]=y
                j+=1
                y=-75
    
    
    for i in range(j):
        pygame.draw.rect(gameDisplay, (255,0,0),figures_on_disp[i])

    for i in range(10):
        if y_base[i] != height_disp:
            point+=1
    
    if point == 10:
        score+=1
        for i in figures_on_disp:
            i[1]+=height_figure
        for i in range(10):
            y_base[i]+=height_figure
        point=0
        #done=True #-----------------------------------------------------------------------------------------SOURE------------------------------------------------------------------------
    else:
        point=0  
    
    pygame.draw.rect(gameDisplay, (255,0,0), [x, y,width_figure,height_figure ])
  
  # --- Game logic should go here
  # --- Drawing code should go here
  # First, clear the screen to white. Don't put other drawing commands
  # above this, or they will be erased with this command.
  #gameDisplay.fill(WHITE)
  # --- Go ahead and update the screen with what we've drawn.
   # pygame.draw.rect(gameDisplay, (255,0,0), [55, 50, 80, 55])
    pygame.display.update()
  # --- Limit to 60 frames per second
    clock.tick(60)