import pygame

from functoins import load_level, load_image, generate_level, move
from settings import *
from start import start_screen

# Инициализируем игру
pygame.init()
screen = pygame.display.set_mode(SIZE)
running = True
clock = pygame.time.Clock()

# Создаем спрайты
tile_group = pygame.sprite.Group()
hero_group = pygame.sprite.Group()
tile_images = {
    'wall': load_image('box.png'),
    'empty': load_image('grass.png')
}
player_image = load_image('mar.png')
level_map = load_level("map.map")
hero = generate_level(level_map, tile_group, hero_group, tile_images, player_image)
start_screen(screen, clock)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                move(hero, level_map, "down")
            if event.key == pygame.K_RIGHT:
                move(hero, level_map, 'right')
            if event.key == pygame.K_LEFT:
                move(hero, level_map, 'left')
            if event.key == pygame.K_UP:
                move(hero, level_map, 'up')
    screen.fill(pygame.Color("black"))
    tile_group.draw(screen)
    hero_group.draw(screen)
    # Отрисовываем тайлы
    # Отрисовываем игрока
    clock.tick(FPS)
    pygame.display.flip()
pygame.quit()
