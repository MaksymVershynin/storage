import pygame
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('hello user')
Clock=pygame.time.Clock()

x=50
y=50
weight=100
height=120
vol=5
flag=True

while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        key=pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        x=x-vol
    elif key[pygame.K_RIGHT]:
        x=x+vol
    elif key[pygame.K_UP]:
        y-=vol
    elif key[pygame.K_DOWN]:
        y+=vol

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255,0,0), [x, y, weight, height],vol)
  
  # --- Game logic should go here
  # --- Drawing code should go here
  # First, clear the screen to white. Don't put other drawing commands
  # above this, or they will be erased with this command.
  #gameDisplay.fill(WHITE)
  # --- Go ahead and update the screen with what we've drawn.
   # pygame.draw.rect(gameDisplay, (255,0,0), [55, 50, 80, 55])
    pygame.display.update()
  # --- Limit to 60 frames per second
    Clock.tick(60)