import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Set up the game clock
CLOCK = pygame.time.Clock()

# Set up the game colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the game fonts
FONT = pygame.font.Font(None, 50)

# Set up the game variables
BALL_RADIUS = 10
BALL_SPEED = 5
BALL_X = WINDOW_WIDTH // 2
BALL_Y = WINDOW_HEIGHT // 2
BALL_DX = random.choice([-1, 1]) * BALL_SPEED
BALL_DY = random.choice([-1, 1]) * BALL_SPEED
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 80
LEFT_PADDLE_X = 50
LEFT_PADDLE_Y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
RIGHT_PADDLE_X = WINDOW_WIDTH - 50 - PADDLE_WIDTH
RIGHT_PADDLE_Y = WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2
LEFT_SCORE = 0
RIGHT_SCORE = 0

# Set up the game functions
def draw_ball(x, y):
    pygame.draw.circle(WINDOW, WHITE, (x, y), BALL_RADIUS)

def draw_paddle(x, y):
    pygame.draw.rect(WINDOW, WHITE, (x, y, PADDLE_WIDTH, PADDLE_HEIGHT))

def draw_score():
    left_score_text = FONT.render(str(LEFT_SCORE), True, WHITE)
    right_score_text = FONT.render(str(RIGHT_SCORE), True, WHITE)
    left_score_x = WINDOW_WIDTH // 2 - 50 - left_score_text.get_width()
    right_score_x = WINDOW_WIDTH // 2 + 50
    score_y = 50
    WINDOW.blit(left_score_text, (left_score_x, score_y))
    WINDOW.blit(right_score_text, (right_score_x, score_y))

def move_ball():
    global BALL_X, BALL_Y, BALL_DX, BALL_DY, LEFT_SCORE, RIGHT_SCORE
    BALL_X += BALL_DX
    BALL_Y += BALL_DY
    if BALL_Y - BALL_RADIUS < 0:
        BALL_Y = BALL_RADIUS
        BALL_DY *= -1
    elif BALL_Y + BALL_RADIUS > WINDOW_HEIGHT:
        BALL_Y = WINDOW_HEIGHT - BALL_RADIUS
        BALL_DY *= -1
    if BALL_X - BALL_RADIUS < 0:
        BALL_X = BALL_RADIUS
        BALL_DX *= -1
        RIGHT_SCORE += 1
    elif BALL_X + BALL_RADIUS > WINDOW_WIDTH:
        BALL_X = WINDOW_WIDTH - BALL_RADIUS
        BALL_DX *= -1
        LEFT_SCORE += 1

def move_paddles():
    global LEFT_PADDLE_Y, RIGHT_PADDLE_Y
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        LEFT_PADDLE_Y -= 5
    elif keys[pygame.K_s]:
        LEFT_PADDLE_Y += 5
    if keys[pygame.K_UP]:
        RIGHT_PADDLE_Y -= 5
    elif keys[pygame.K_DOWN]:
        RIGHT_PADDLE_Y += 5
    if LEFT_PADDLE_Y < 0:
        LEFT_PADDLE_Y = 0
    elif LEFT_PADDLE_Y + PADDLE_HEIGHT >
