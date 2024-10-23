import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Doodle Jump")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Platform properties
PLATFORM_WIDTH, PLATFORM_HEIGHT = 70, 10
PLATFORM_COLOR = GREEN
MOVING_PLATFORM_COLOR = RED
DISAPPEARING_PLATFORM_COLOR = (200, 200, 200)

# Player properties
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 50
PLAYER_COLOR = BLACK
PLAYER_JUMP = 15

# Game settings
GRAVITY = 1
FPS = 60
FONT = pygame.font.Font(None, 36)

# Player class
class Player:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH//2 - PLAYER_WIDTH//2, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.y_velocity = 0
        self.on_platform = False
        self.score = 0

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Wrap around the screen
        if self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.left > WIDTH:
            self.rect.right = 0

    def jump(self):
        if self.on_platform or self.rect.bottom >= HEIGHT:
            self.y_velocity = -PLAYER_JUMP

    def update(self, platforms):
        self.y_velocity += GRAVITY
        self.rect.y += self.y_velocity

        if self.rect.top <= HEIGHT // 3:
            self.rect.y += abs(self.y_velocity)
            self.score += abs(self.y_velocity)

            for platform in platforms:
                platform.rect.y += abs(self.y_velocity)
                if platform.rect.top > HEIGHT:
                    platform.rect.y = random.randint(-100, -10)
                    platform.rect.x = random.randint(0, WIDTH - PLATFORM_WIDTH)
                    platform.type = random.choice(["normal", "moving", "disappearing"])
                    if platform.type == "moving":
                        platform.direction = random.choice([-1, 1])
                    elif platform.type == "disappearing":
                        platform.visible = True

        self.on_platform = False
        for platform in platforms:
            if platform.type == "disappearing" and platform.visible:
                if self.rect.colliderect(platform.rect) and self.y_velocity > 0:
                    platform.visible = False
                    self.y_velocity = -PLAYER_JUMP
                    self.on_platform = True
            elif self.rect.colliderect(platform.rect) and self.y_velocity > 0:
                self.y_velocity = -PLAYER_JUMP
                self.on_platform = True

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.y_velocity = 0

    def draw(self):
        pygame.draw.rect(screen, PLAYER_COLOR, self.rect)

# Platform class
class Platform:
    def __init__(self, x, y, platform_type="normal"):
        self.rect = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        self.type = platform_type
        self.direction = random.choice([-1, 1]) if platform_type == "moving" else 0
        self.visible = True if platform_type != "disappearing" else random.choice([True, False])

    def update(self):
        if self.type == "moving":
            self.rect.x += self.direction * 2
            if self.rect.left < 0 or self.rect.right > WIDTH:
                self.direction *= -1

    def draw(self):
        if self.type == "normal":
            pygame.draw.rect(screen, PLATFORM_COLOR, self.rect)
        elif self.type == "moving":
            pygame.draw.rect(screen, MOVING_PLATFORM_COLOR, self.rect)
        elif self.type == "disappearing" and self.visible:
            pygame.draw.rect(screen, DISAPPEARING_PLATFORM_COLOR, self.rect)

def create_platforms(num_platforms):
    platforms = []
    for _ in range(num_platforms):
        x = random.randint(0, WIDTH - PLATFORM_WIDTH)
        y = random.randint(0, HEIGHT - PLATFORM_HEIGHT)
        platform_type = random.choice(["normal", "moving", "disappearing"])
        platforms.append(Platform(x, y, platform_type))
    return platforms

def game_over_screen(score):
    screen.fill(WHITE)
    game_over_text = FONT.render("Game Over", True, BLACK)
    score_text = FONT.render(f"Score: {int(score)}", True, BLACK)
    screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 50))
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 + 10))
    pygame.display.flip()

    pygame.time.wait(2000)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Main game loop
def main():
    clock = pygame.time.Clock()
    player = Player()
    platforms = create_platforms(6)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.move()
        player.jump()
        player.update(platforms)

        if player.rect.top > HEIGHT:
            game_over_screen(player.score)
            return

        for platform in platforms:
            platform.update()

        screen.fill(WHITE)
        for platform in platforms:
            platform.draw()
        player.draw()

        score_text = FONT.render(f"Score: {int(player.score)}", True, BLACK)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
