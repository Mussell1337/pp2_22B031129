import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen dimensions
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the font for displaying score and level
font = pygame.font.Font(None, 30)

# Set up the snake's initial position and velocity
snake_position = [300, 300]
snake_body = [[300, 300], [280, 300], [260, 300]]
snake_velocity = [20, 0]

# Set up the initial food position
food_position = [random.randrange(1, (screen_width//20)) * 20,
                 random.randrange(1, (screen_height//20)) * 20]

# Set up the initial game score and level
score = 0
level = 1

# Main game loop
while True:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Check for user input to change snake velocity
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_velocity = [-20, 0]
    elif keys[pygame.K_RIGHT]:
        snake_velocity = [20, 0]
    elif keys[pygame.K_UP]:
        snake_velocity = [0, -20]
    elif keys[pygame.K_DOWN]:
        snake_velocity = [0, 20]

    # Move the snake
    snake_position[0] += snake_velocity[0]
    snake_position[1] += snake_velocity[1]

    # Check for border collision
    if snake_position[0] < 0 or snake_position[0] > screen_width-20:
        pygame.quit()
        quit()
    elif snake_position[1] < 0 or snake_position[1] > screen_height-20:
        pygame.quit()
        quit()

    # Check if the snake has eaten the food
    if snake_position == food_position:
        food_position = [random.randrange(1, (screen_width//20)) * 20,
                         random.randrange(1, (screen_height//20)) * 20]
        score += 1

        # Increase speed and level every 3-4 foods
        if score % 3 == 0 or score % 4 == 0:
            level += 1
            snake_velocity[0] += 2
            snake_velocity[1] += 2

        # Add another block to the snake's body
        snake_body.insert(0, list(snake_position))

    # Move the snake's body
    for block in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(
            block[0], block[1], 20, 20))

    # Draw the food
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(
        food_position[0], food_position[1], 20, 20))

    # Update the score and level display
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    screen.blit(score_text, (5, 10))
    screen.blit(level_text, (5, 30))

    # Update the screen
    pygame.display.update()

    # Move the snake's body by updating its position
    snake_body.insert(0, list(snake_position))
    if snake_position != food_position:
        snake_body.pop()

    # Check for collision with the snake's body
    for block in snake_body[1:]:
        if snake_position == block:
            pygame.quit()
            quit()

    # Clear the screen for the next frame
    screen.fill((0, 0, 0))

    # Set the game's FPS
    clock.tick(10 + level)

# Quit pygame
pygame.quit()
quit()