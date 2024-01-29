import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Flappy Bird")

rect1_x = 40
rect1_y = 220
rect2_x = 400
rect2_y = 400 
rect3_x = 400
rect3_y = 0
speed = 1.5
rect2_height = 200
rect3_height = 200
pipe1_passed = False

player_rect = pygame.Rect(rect1_x, rect1_y, 70, 70)
pipe1_rect = pygame.Rect(rect2_x, rect2_y, 90, rect2_height)
pipe2_rect = pygame.Rect(rect3_x, rect3_y, 90, rect3_height)

pipe1_initial_x = rect2_x
score = 0

def draw():

  screen.fill((255, 255, 255))

  font = pygame.font.Font(None, 36)
  text = font.render(str(score), True, (169, 169, 169))

  player_rect.x = rect1_x
  player_rect.y = rect1_y

  pipe1_rect.x = rect2_x
  pipe1_rect.y = rect2_y
  pipe1_rect.height = rect2_height

  pipe2_rect.x = rect3_x 
  pipe2_rect.y = rect3_y
  pipe2_rect.height = rect3_height

  pygame.draw.rect(screen, (255, 0, 0), player_rect)
  pygame.draw.rect(screen, (0, 0, 0), pipe1_rect)
  pygame.draw.rect(screen, (0, 0, 0), pipe2_rect)

  screen.blit(text, (700, 50))

running = True
while running:

  rect1_y += 0.4
  keys = pygame.key.get_pressed()
  if keys[pygame.K_SPACE]:
    rect1_y -= 1          
    if rect1_y < 0:
      rect1_y = 0

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

  if player_rect.colliderect(pipe1_rect) or player_rect.colliderect(pipe2_rect): 
    pygame.time.delay(3000)
    running = False

  if pipe1_rect.x > pipe1_initial_x: 
    pipe1_passed = True
    score += 1

  if pipe1_rect.x < 0:
    pipe1_passed = False
    pipe1_initial_x = 800

  rect2_x -= speed
  rect3_x -= speed  

  if rect2_x < 0:
    rect2_x = 800
    rect2_height = random.randint(100, 270)
    rect2_y = 600 - rect2_height

  if rect3_x < 0:
    rect3_x = 800
    rect3_height = random.randint(100,250)
    rect3_y = 0

  if rect1_y > 600 - 70:
    rect1_y = 600 - 70

  draw()

  pygame.display.flip()

pygame.quit()
