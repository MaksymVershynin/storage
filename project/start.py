import pygame
pygame.init()
gameDisplay=pygame.display.set_mode((400,300))
pygame.display.set_caption("My first game")
clock=pygame.time.Clock()

x=50
y=50
width=40
height=60
vol=5

WHITE = (255, 255, 255)  
ORANGE = (255, 150, 100)
BLACK = (0,0,0)
# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
# -------- Main Program Loop -----------
while not done:
  # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x>vol:
            x=x-vol
    if keys[pygame.K_RIGHT] and x<(400-width-vol):
            x=x+vol
    if keys[pygame.K_UP] and y>vol:
            y=y-vol
    if keys[pygame.K_DOWN] and y<(300 - height-vol):
            y=y+vol

    gameDisplay.fill((0,0,0))
    pygame.draw.rect(gameDisplay, (255,0,0), [x, y, width, height],vol)
  
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