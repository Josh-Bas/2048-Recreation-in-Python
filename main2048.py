import pygame as pg
from data.helper2048 import *
from sys import exit

pg.init()

# Basic game settings
screen = pg.display.set_mode((429,580))
pg.display.set_caption('2048')
clock = pg.time.Clock()
running = True
player_input_enabled = True
win, show_win_screen, win_condition_triggered = False, False, False

# 2D array to track the values of the tiles
grid = make_grid()

# Fonts
score_font = pg.font.Font(None, 40)

# Surfaces
background = pg.image.load('data/images/background.jpg').convert()
win_screen = pg.image.load('data/images/congrat.jpg').convert()
score = score_font.render('0', True, 'white')
newgame_rect = pg.Rect((245,118), (157, 54))
tile_images = load_tile_images()


add_random_tile(grid)
# Main game loop
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        # Resets the grid if player presses new game button
        elif event.type == pg.MOUSEBUTTONDOWN and player_input_enabled:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if newgame_rect.collidepoint(mouse_x, mouse_y):
                new_game(grid)

        # Handles player input
        elif event.type == pg.KEYDOWN and player_input_enabled:
            if event.key == pg.K_UP:
                shift_up_down(grid, "up")
                add_random_tile(grid)
            elif event.key == pg.K_DOWN:
                shift_up_down(grid, "down")
                add_random_tile(grid)
            elif event.key == pg.K_LEFT:
                shift_left_right(grid, "left")
                add_random_tile(grid)
            elif event.key == pg.K_RIGHT:
                shift_left_right(grid, "right")
                add_random_tile(grid)

    # Blits the various surfaces onto the window
    screen.blit(background, (0,0))
    screen.blit(score, (260, 54))
    screen.blit(score, (350, 54))

    # Draws the grid
    draw_grid(tile_images, grid, screen)

    # Win screen is displayed for 10 seconds if win is true
    if not win_condition_triggered:
        win = check_win(grid)
        win_condition_triggered = win
    if win_condition_triggered and win:
        show_win_screen = True
        win_screen_start_time = pg.time.get_ticks()
        win = False
    if show_win_screen:
        current_time = pygame.time.get_ticks()
        if current_time - win_screen_start_time < 10000:
            player_input_enabled = False
            screen.blit(win_screen, (0, 113))
        else:
            player_input_enabled = True
            show_win_screen = False

    # Update the screen
    pg.display.update()
    clock.tick(60)


pg.quit()