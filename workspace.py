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
background = pygame.image.load("baba_yaga/imgs/menus/main_menu/baba_yaga_menu_background.png")
while (running == True):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background,(0,0))
    pygame.display.flip()

program_clock.tick(60)

print("quiting pygame")
pygame.display.quit()
pygame.quit()
print("pygame ended")