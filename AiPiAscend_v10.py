
import pygame
import sys
import random

# Initialization
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('AiPi Ascend')
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 128, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Fonts
font = pygame.font.SysFont(None, 36)

score = 0

def display_score():
    score_display = font.render(f"Score: {score}", True, BLUE)
    screen.blit(score_display, (SCREEN_WIDTH - 120, 10))

def display_health(health):
    health_display = font.render(f"Health: {health}", True, RED)
    screen.blit(health_display, (10, 10))

# Player mechanics
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60)
        self.velocity = [0, 0]
        self.gravity = 1
        self.jump_strength = -15
        self.on_ground = False
        self.health = 100

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.velocity[0] = -5
        elif keys[pygame.K_RIGHT]:
            self.velocity[0] = 5
        else:
            self.velocity[0] = 0

        if self.on_ground and keys[pygame.K_UP]:
            self.velocity[1] = self.jump_strength

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Temporary floor collision
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.velocity[1] = 0
            self.on_ground = True
        else:
            self.on_ground = False

# Platforms

# Platforms
class Platform(pygame.sprite.Sprite):
    
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.choice([-2, -1, 1, 2])  # Platforms can move horizontally in both directions

        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.speed = random.choice([-2, -1, 0, 1, 2])  # Platforms can have horizontal movement
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.choice([-2, -1, 0, 1, 2])  # Platforms can have horizontal movement

    def update(self):
        self.rect.x += self.speed
        # Wrap around the screen
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH
        elif self.rect.left > SCREEN_WIDTH:
            self.rect.right = 0

    
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = random.choice([-2, -1, 1, 2])  # Platforms can move horizontally in both directions

        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.speed = random.choice([-2, -1, 0, 1, 2])  # Platforms can have horizontal movement
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

player = Player()
platforms = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites.add(player)

# Create initial platforms
for i in range(5):
    p = Platform(i * (SCREEN_WIDTH // 5), SCREEN_HEIGHT - (i * 70), random.randint(50, 100), 10)
    platforms.add(p)
    all_sprites.add(p)

def game_loop():
    global score
    run_game = True
    while run_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        keys = pygame.key.get_pressed()
        player.move(keys)
        
        # Update game state
        all_sprites.update()
        platform_collision = pygame.sprite.spritecollide(player, platforms, False)
        if platform_collision:
            player.rect.bottom = platform_collision[0].rect.top
            player.on_ground = True
            player.velocity[1] = 0
        else:
            player.on_ground = False
        
        # Render game state
        screen.fill(WHITE)
        display_score()
        all_sprites.draw(screen)
        display_health(player.health)
        bullets.draw(screen)
        
        pygame.display.flip()
        
        
        # Increase score when climbing upwards
        if player.velocity[1] < 0:
            score += 1

            score += 1
        
        clock.tick(FPS)

# Start the game loop
game_loop()
