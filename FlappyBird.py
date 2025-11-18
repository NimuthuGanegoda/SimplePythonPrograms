import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()

WIDTH = 448
HEIGHT = 600
FLOOR_Y = 520

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Flappy Bird")
font = pygame.font.SysFont("arial", 28)

# Game variables
gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0

# Surfaces (placeholder graphics; replace with images if available)
bird_surface = pygame.Surface((34, 24))
bird_surface.fill((255, 255, 0))
bird_rect = bird_surface.get_rect(center=(100, HEIGHT // 2))

floor_surface = pygame.Surface((WIDTH, 80))
floor_surface.fill((220, 180, 120))
floor_x_pos = 0

pipe_img = pygame.Surface((70, 400))
pipe_img.fill((60, 200, 60))
pipe_height = [300, 350, 400, 450]

pipes = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, FLOOR_Y))
    screen.blit(floor_surface, (floor_x_pos + WIDTH, FLOOR_Y))

def create_pipe():
    pip_y = random.choice(pipe_height)
    top_pipe = pipe_img.get_rect(midbottom=(WIDTH + 20, pip_y - 250))
    bottom_pipe = pipe_img.get_rect(midtop=(WIDTH + 20, pip_y))
    return top_pipe, bottom_pipe

def pipe_animation():
    global game_active
    for p in list(pipes):
        if p.top < 0:
            flipped_pipe = pygame.transform.flip(pipe_img, False, True)
            screen.blit(flipped_pipe, p)
        else:
            screen.blit(pipe_img, p)
        p.centerx -= 3
        if p.right < 0:
            pipes.remove(p)
        if bird_rect.colliderect(p):
            game_active = False

def rotate_bird(surface, movement):
    return pygame.transform.rotozoom(surface, -movement * 3, 1)

def score_display(game_state):
    if game_state == 'main_game':
        score_surface = font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(WIDTH // 2, 50))
        screen.blit(score_surface, score_rect)
    elif game_state == 'game_over':
        score_surface = font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(WIDTH // 2, 50))
        screen.blit(score_surface, score_rect)
        high_score_surface = font.render(f'High Score: {int(high_score)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center=(WIDTH // 2, 90))
        screen.blit(high_score_surface, high_score_rect)
        restart_surface = font.render('Press SPACE to Restart', True, (255, 255, 255))
        restart_rect = restart_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(restart_surface, restart_rect)

def update_score(sc):
    return sc + 0.01

def check_passed_pipes():
    global score
    for p in pipes:
        if p.centerx == bird_rect.centerx:
            score += 1

def reset_game():
    global pipes, bird_rect, bird_movement, score, game_active
    pipes = []
    bird_rect.center = (100, HEIGHT // 2)
    bird_movement = 0
    score = 0
    game_active = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 7
            elif event.key == pygame.K_SPACE and not game_active:
                reset_game()
        if event.type == SPAWNPIPE and game_active:
            pipes.extend(create_pipe())

    screen.fill((30, 30, 30))

    if game_active:
        bird_movement += gravity
        bird_rect.centery += bird_movement
        rotated_bird = rotate_bird(bird_surface, bird_movement)
        screen.blit(rotated_bird, bird_rect)

        pipe_animation()

        # Floor scrolling
        floor_x_pos -= 2
        if floor_x_pos <= -WIDTH:
            floor_x_pos = 0
        draw_floor()

        # Collision with top/bottom bounds
        if bird_rect.top <= -50 or bird_rect.bottom >= FLOOR_Y:
            game_active = False

        score = update_score(score)
        score_display('main_game')
    else:
        if score > high_score:
            high_score = score
        score_display('game_over')
        draw_floor()

    pygame.display.update()
    clock.tick(120)