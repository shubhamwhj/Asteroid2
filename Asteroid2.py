import pygame, random, sys


pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Asteroid")
background_image = pygame.image.load("bg2.jpg").convert()


#Color or rectangle
BLUE=(0,0,255)
player=pygame.Rect(200,200,30,30)


WHITE=(255,255,255)
enemy=pygame.Rect(100,100,30,30)
xvel=2
yvel=3

while True:
  screen.blit(background_image,[0,0])
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      
  
  enemy.x=enemy.x + xvel
  enemy.y=enemy.y + yvel 
  
  if enemy.x < -250 or enemy.x > 650 :
    xvel = -1*xvel
  
  if enemy.y < -250 or enemy.y > 850:  
    yvel = -1*yvel

  pygame.draw.rect(screen,BLUE,player)
  pygame.draw.rect(screen,WHITE,enemy)

  pygame.display.update()
  clock.tick(30)
  
  
