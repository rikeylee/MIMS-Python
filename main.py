import pygame
import random

# Initialize Pygame
pygame.init()

# Game Window Setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Atom's Adventure")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# FPS (frames per second)
FPS = 60
clock = pygame.time.Clock()

# Character setup
ATOM_WIDTH = 50
ATOM_HEIGHT = 60
atom_x = 100
atom_y = HEIGHT - ATOM_HEIGHT
atom_velocity = 5
jumping = False
y_velocity = 0

# Load Atom's character image (with wig)
atom_image = pygame.Surface((ATOM_WIDTH, ATOM_HEIGHT))  # Placeholder for image
atom_image.fill(RED)

# Create a simple wig (just a small rectangle on top of Atom)
wig_width = 40
wig_height = 10
wig = pygame.Surface((wig_width, wig_height))
wig.fill((255, 255, 0))  # Yellow wig

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
    if keys[pygame.K_RIGHT]:
        atom_x += atom_velocity

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
    screen.blit(atom_image, (atom_x, atom_y))
    screen.blit(wig, (atom_x + 5, atom_y - wig_height))  # Wig slightly above Atom’s head

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(FPS)

pygame.quit()
