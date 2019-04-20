import random
import pygame
pygame.init()

#resolution of display
height_disp=925
width_disp=1050

gameDisplay=pygame.display.set_mode((width_disp,height_disp))
pygame.display.set_caption("TETRIS")
clock=pygame.time.Clock()
font = pygame.font.SysFont('Calibri', 25, True, False)
fontStart = pygame.font.SysFont('Calibri', 200, True, False)
fontStart1 = pygame.font.SysFont('Calibri', 50,False,True)
fontStart2 = pygame.font.SysFont('Calibri', 10,False,True)

figure_step=100
point=0
score=0
j=1

y_base=[height_disp for i in range(10)]   # initial field for figures
figures_on_disp =[[0,0,0,0]]              # list of figure`s parametrs on display

# position for first figure
x=525
y=25
width_figure=100
height_figure=100



ORANGE = (255, 150, 100)
GRAY = (128, 128, 128)


#--------------Start screen--------------
textStart = fontStart.render("TETRIS",True,ORANGE)
gameDisplay.blit(textStart, [250,200])
textStart1 = fontStart1.render("simplified version for young children",True,ORANGE)
gameDisplay.blit(textStart1, [175,400])
textStart2 = fontStart1.render("to continue press 'Space'",True,GRAY)
gameDisplay.blit(textStart2, [475,800])
pygame.display.update()
do = True
while do:
    for event in pygame.event.get():
        key=pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        do = False


        
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
    
    #text "score" on display
    text = font.render("SCORE: " + str(score),True,ORANGE)
    gameDisplay.blit(text, [900, 50])


    # moving figure to down    
    if y<=(height_disp-height_figure-figure_step):
        y+=figure_step

        
    #lets give our figures opportunity stay on the display ;)
    for i in range(10):
        if x==(i*width_figure+25):#--------------------------------------------- 25 - that frame ondisplay
            if (y+height_figure==y_base[i]):
                figures_on_disp.append([x,y,width_figure,height_figure])
                y_base[i]=y
                j+=1 #---------------------------------------------------------- amount of figures
                y=-75 #--------------------------------------------------------- next figure will start from top
    
    #drawing figures on display
    for i in range(j):
        pygame.draw.rect(gameDisplay, (255,0,0),figures_on_disp[i])

    #------------------------------------------------lets check, may be you earn a score!!!
    point=0
    for i in range(10):
        if y_base[i] != height_disp:
            point+=1
    
    if point == 10:
        score+=1
        for i in figures_on_disp:
            i[1]+=height_figure
        for i in range(10):
            y_base[i]+=height_figure
    

    #drawing figure which is falling down 
    pygame.draw.rect(gameDisplay, (255,0,0), [x, y,width_figure,height_figure ])
  

    pygame.display.update()
    # --- Limit to 60 frames per second
    clock.tick(60)