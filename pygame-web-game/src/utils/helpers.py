def load_image(file_path):
    import pygame
    try:
        image = pygame.image.load(file_path)
        return image
    except pygame.error as e:
        print(f"Unable to load image at {file_path}: {e}")
        return None

def load_sound(file_path):
    import pygame
    try:
        sound = pygame.mixer.Sound(file_path)
        return sound
    except pygame.error as e:
        print(f"Unable to load sound at {file_path}: {e}")
        return None

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

def reset_game_state():
    # Reset game variables to their initial state
    pass