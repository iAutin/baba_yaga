import pygame, sys

print("launching pygame")
pygame.init()

program_clock = pygame.time.Clock()

screen_width = 1366
screen_height = 768

pygame.display.init()
screen = pygame.display.set_mode([screen_width,screen_height])

running = True
time = 0
while (running == True):
    time = time + 1
    if (time == 10000):
        running = False
    pygame.display.flip()
program_clock.tick(60)

print("quiting pygame")
pygame.display.quit()
pygame.quit()
print("pygame ended")