import pygame
import random

# initialize pygame
pygame.init()

# set up the game window
window_width = 500
window_height = 500
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# define the snake class
class Snake:
    def __init__(self):
        self.size = 10
        self.x = window_width / 2
        self.y = window_height / 2
        self.dx = self.size
        self.dy = 0
        self.body = []
        self.length = 1

    def draw(self):
        for x, y in self.body:
            pygame.draw.rect(window, white, [x, y, self.size, self.size])

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.body.append((self.x, self.y))
        if len(self.body) > self.length:
            del self.body[0]

    def check_collision(self):
        if self.x < 0 or self.x > window_width - self.size or self.y < 0 or self.y > window_height - self.size:
            return True
        for x, y in self.body[:-1]:
            if self.x == x and self.y == y:
                return True
        return False

    def eat_food(self, food):
        if self.x == food.x and self.y == food.y:
            self.length += 1
            return True
        return False

# define the food class
class Food:
    def __init__(self):
        self.size = 10
        self.x = random.randint(0, window_width - self.size)
        self.y = random.randint(0, window_height - self.size)

    def draw(self):
        pygame.draw.rect(window, red, [self.x, self.y, self.size, self.size])

# set up the game loop
snake = Snake()
food = Food()
clock = pygame.time.Clock()
score = 0
game_over = False

while not game_over:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.dx = -snake.size
                snake.dy = 0
            elif event.key == pygame.K_RIGHT:
                snake.dx = snake.size
                snake.dy = 0
            elif event.key == pygame.K_UP:
                snake.dx = 0
                snake.dy = -snake.size
            elif event.key == pygame.K_DOWN:
                snake.dx = 0
                snake.dy = snake.size

    # update the snake and food
    snake.move()
    if snake.check_collision():
        game_over = True
    if snake.eat_food(food):
        food = Food()
        score += 10

    # draw the game objects
    window.fill(black)
    snake.draw()
    food.draw()
    pygame.display.update()

    # set the game speed
    clock.tick(10)

# display the final score
font = pygame.font.SysFont(None, 30)
text = font.render("Final Score: " + str(score), True, white)
window.blit(text, (window_width / 2 - text.get_width() / 2, window_height / 2 - text.get_height() / 2))
pygame.display.update()

# wait for the user to close the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()