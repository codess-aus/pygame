import sys
import os  # Add this line to import the os module
import pygame

# Disable audio by setting SDL_AUDIODRIVER to "dummy"
os.environ["SDL_AUDIODRIVER"] = "dummy"

# Disable audio to suppress ALSA errors in headless environments
pygame.mixer.quit()

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 650, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Turtle Graphics Game")

# Set up colors
NAVY = (0, 0, 128)
DARK_ORANGE = (255, 140, 0)

# Create player properties
player_pos = [WIDTH // 2, HEIGHT // 2]
player_speed = 1
player_size = 20

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the player
    player_pos[0] += player_speed

    # Fill the background
    screen.fill(NAVY)

    # Draw the player
    pygame.draw.circle(screen, DARK_ORANGE, player_pos, player_size)

    # Update the display
    pygame.display.flip()

    # Save the current frame to an image file for debugging
    pygame.image.save(screen, "screenshot.png")

    # Cap the frame rate
    pygame.time.Clock().tick(60)