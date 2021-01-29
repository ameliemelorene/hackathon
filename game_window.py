import pygame
import sys

# Création de la fenêtre de jeu

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700

# RECT = JOUEUR
RECT_WIDTH = 20
RECT_HEIGHT = 20

# Font --> ?

pygame.init()

game_window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Sur la piste du Stade Rennais")

game_running = True
clock = pygame.time.Clock()

# Start player in center of screen
x_pos = WINDOW_WIDTH / 2 - RECT_WIDTH / 2
y_pos = WINDOW_HEIGHT / 2 - RECT_HEIGHT / 2
x_vel = 0
y_vel = 0

# Game Loop

while game_running:
    # Loop through all active events
    for event in pygame.event.get():
    # Close the program if the user presses the 'X'
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_vel -= 5
            elif event.key == pygame.K_DOWN:
                y_vel += 5
            elif event.key == pygame.K_LEFT:
                x_vel -= 5
            elif event.key == pygame.K_RIGHT:
                x_vel += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_vel -= 5
            if event.key == pygame.K_LEFT:
                x_vel += 5
            if event.key == pygame.K_UP:
                y_vel += 5
            if event.key == pygame.K_DOWN:
                y_vel -= 5
    # White background window
    game_window.fill((255,255,255))

    # Update rect position
    x_pos += x_vel
    y_pos += y_vel
    filled_rect = pygame.Rect(x_pos, y_pos, RECT_WIDTH, RECT_HEIGHT)
    pygame.draw.rect(game_window, (25,100,178), filled_rect)
    pygame.display.update()
    clock.tick(20)

pygame.quit()
sys.exit()