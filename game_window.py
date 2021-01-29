import pygame
import sys

# Création de la fenêtre de jeu

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700

pygame.init()

game_window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("La quête de Sœur Thérèse")

game_running = True

# Game Loop

while game_running:
    # Loop through all active events
    for event in pygame.event.get():
    # Close the program if the user presses the 'X'
    if event.type == pygame.QUIT:
        game_running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            print("Move the character forwards")
        elif event.key == pygame.K_s:
            print("Move the character backwards")
        elif event.key == pygame.K_a:
            print("Move the character left")
        elif event.key == pygame.K_d:
            print("Move the character right")
    game_window.fill((255,255,255))
    pygame.display.update()

pygame.quit()
sys.exit()