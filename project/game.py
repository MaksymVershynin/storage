import random
import pygame
pygame.init()

#resolution of display
height_disp=925
width_disp=1050

gameDisplay=pygame.display.set_mode((width_disp,height_disp))
pygame.display.set_caption("TETRIS")
clock=pygame.time.Clock()

figure_step=50
re=0
k=1
x=525
y=25
width_figure=random.randint(1,3)*50
height_figure=random.randint(1,3)*50
y_base=[height_disp for i in range(20)]

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

    #Here figure has been stay on display
    #--------------------------------------------------------------------------------------------------------------------------
    
    
    # if (y+height_figure)==(height_disp):
    #     figures_on_disp.append([x,y,width_figure,height_figure])
    #     height_current=y
    #     j+=1
    #     y=-25
    #     width_figure=random.randint(1,3)*50
    #     height_figure=random.randint(1,3)*50

    
    #--------------------------------------------------------------------------------------------------------------------------
    # moving figure to down

    y+=figure_step
    #--------------------------------------------------------------------------------------------------------------------------
    for j in range(int(width_figure/50+1)):
        for i in range(20):
            if (x+j*50)==(i*50+25):
                if (y+height_figure==y_base[i+j]):
                    figures_on_disp.append([x,y,width_figure,height_figure])
                    y_base[i+j]=y
                    k+=1
                    re=1
    



    for i in range(k):
        pygame.draw.rect(gameDisplay, (255,0,0),figures_on_disp[i])
    

    if re==1:
        y=-25
        re=0                
        width_figure=random.randint(1,3)*50
        height_figure=random.randint(1,3)*50


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