import pygame
import random

# Initialize Pygame
pygame.init()

# Game Window Setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Atom's Adventure")
facing_right = True  # Track direction

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# FPS (frames per second)
FPS = 60
clock = pygame.time.Clock()

# Character setup
ATOM_WIDTH = 100
ATOM_HEIGHT = 120
atom_x = 100
atom_y = HEIGHT - ATOM_HEIGHT
atom_velocity = 5
jumping = False
y_velocity = 0

# Load Atom's character image (with wig)
atom_image = pygame.image.load("images/atom.png").convert_alpha()
atom_image = pygame.transform.scale(atom_image, (ATOM_WIDTH, ATOM_HEIGHT))

# 

# Gravity & Jumping
gravity = 0.8
jump_strength = -15

# Power-ups
power_ups = []

# Main Game Loop
running = True
while running:
    screen.fill(WHITE)
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keypresses for movement
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        atom_x -= atom_velocity
        facing_right = False
    if keys[pygame.K_RIGHT]:
        atom_x += atom_velocity
        facing_right = True

    # Jumping mechanic
    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
            y_velocity = jump_strength

    # Apply gravity
    if jumping:
        atom_y += y_velocity
        y_velocity += gravity
        if atom_y >= HEIGHT - ATOM_HEIGHT:
            atom_y = HEIGHT - ATOM_HEIGHT
            jumping = False
            y_velocity = 0

    # Draw Atom and wig
    flipped_image = pygame.transform.flip(atom_image, True, False) if facing_right else atom_image
    screen.blit(flipped_image, (atom_x, atom_y))
    
    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(FPS)

pygame.quit()
