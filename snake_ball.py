import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake and Ball Game")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
WHITE = (255, 255, 255)

# Game settings
snake_size = 15
snake_speed = 10

# Fonts
font = pygame.font.SysFont("arial", 25)

# Snake and ball initialization
snake = [(100, 50), (90, 50), (80, 50)]
direction = "RIGHT"
ball_pos = [random.randrange(1, (WIDTH // snake_size)) * snake_size,
            random.randrange(1, (HEIGHT // snake_size)) * snake_size]

clock = pygame.time.Clock()

def draw_snake(snake_list):
    for pos in snake_list:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], snake_size, snake_size))

def message(msg, color):
    text = font.render(msg, True, color)
    screen.blit(text, [WIDTH / 6, HEIGHT / 3])

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # Move the snake
    x, y = snake[0]
    if direction == "UP":
        y -= snake_size
    elif direction == "DOWN":
        y += snake_size
    elif direction == "LEFT":
        x -= snake_size
    elif direction == "RIGHT":
        x += snake_size

    # Check wall collision
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        screen.fill(BLACK)
        message("💀 Game Over! Press ESC to quit", RED)
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        continue

    # Update snake position
    snake.insert(0, (x, y))

    # Check ball collision
    if x == ball_pos[0] and y == ball_pos[1]:
        ball_pos = [random.randrange(1, (WIDTH // snake_size)) * snake_size,
                    random.randrange(1, (HEIGHT // snake_size)) * snake_size]
    else:
        snake.pop()

    # Check self collision
    if (x, y) in snake[1:]:
        screen.fill(BLACK)
        message("💀 Game Over! Press ESC to quit", RED)
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        continue

    # Draw everything
    screen.fill(BLACK)
    draw_snake(snake)
    pygame.draw.rect(screen, RED, pygame.Rect(ball_pos[0], ball_pos[1], snake_size, snake_size))

    pygame.display.update()
    clock.tick(snake_speed)