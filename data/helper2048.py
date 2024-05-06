import pygame
from random import choice
GRID_SIZE = 4

tile_pos = {(0,0):(38,192),
            (0,1):(128,192),
            (0,2):(218,192),
            (0,3):(308,192),
            (1,0):(38,282),
            (1,1):(128,282),
            (1,2):(218,282),
            (1,3):(308,282), 
            (2,0):(38,372), 
            (2,1):(128,372),
            (2,2):(218,372),
            (2,3):(308,372),
            (3,0):(38,462),
            (3,1):(128,462),
            (3,2):(218,462),
            (3,3):(308,462)
            }


# 2D array to track the values of the tiles
def make_grid():
    grid = [[0 for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
    return grid


# Loads images of the tiles and returns them in a dictionary
def load_tile_images():
    two = pygame.image.load('data/images/2.png').convert()
    four = pygame.image.load('data/images/4.png').convert()
    eight = pygame.image.load('data/images/8.png').convert()
    sixteen = pygame.image.load('data/images/16.png').convert()
    thirtytwo = pygame.image.load('data/images/32.png').convert()
    sixtyfour = pygame.image.load('data/images/64.png').convert()
    onetwoeight = pygame.image.load('data/images/128.png').convert()
    twofivesix = pygame.image.load('data/images/256.png').convert()
    fivetwelve = pygame.image.load('data/images/512.png').convert()
    tentwentyfour = pygame.image.load('data/images/1024.png').convert()
    twentyfourtyeight = pygame.image.load('data/images/2048.png').convert()
    fourtyninetysix = pygame.image.load('data/images/4096.png').convert()
    tile_names = {
        2: two,
        4: four,
        8: eight,
        16: sixteen,
        32: thirtytwo,
        64: sixtyfour,
        128: onetwoeight,
        256: twofivesix,
        512: fivetwelve,
        1024: tentwentyfour,
        2048: twentyfourtyeight,
        4096: fourtyninetysix
    }
    return tile_names


# Add a random tile at the position of a random empty tile
def add_random_tile(grid):
    empty_cells = [(i,j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 0]
    if empty_cells:
        i, j = choice(empty_cells)
    else:
        return
    grid[i][j] = choice([2, 4])
    return


# Blits the tiles based on the grid
def draw_grid(tile_images, grid, screen):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            value = grid[i][j]
            if value != 0:
                screen.blit(tile_images[value], tile_pos[(i,j)])
    return


# Merges the elements in the grid and then shifts them left or right
def shift_left_right(grid, direction):
    for row in grid:
        non_zero_elements = [element for element in row if element != 0]
        
        merged_elements = []
        i = 0
        while i < len(non_zero_elements):
            if i + 1 < len(non_zero_elements) and non_zero_elements[i] == non_zero_elements[i + 1]:
                merged_elements.append(non_zero_elements[i] * 2)
                i += 2
            else:
                merged_elements.append(non_zero_elements[i])
                i += 1

        zeroes_to_pad = len(row) - len(merged_elements)
        if direction == "right":
            row[:] = [0] * zeroes_to_pad + merged_elements
        elif direction == "left":
            row[:] = merged_elements + [0] * zeroes_to_pad
    return


# Merges the elements in the grid and then shifts them up or down
def shift_up_down(grid, direction):
    for col in range(GRID_SIZE): #  CHANGE TO GRID SIZE
        non_zero_elements = [grid[row][col] for row in range(GRID_SIZE) if grid[row][col] != 0]

        merged_elements = []
        i = 0
        while i < len(non_zero_elements):
            if i + 1 < len(non_zero_elements) and non_zero_elements[i] == non_zero_elements[i + 1]:
                
                merged_elements.append(non_zero_elements[i] * 2)
                i += 2
            else:
                merged_elements.append(non_zero_elements[i])
                i += 1

        zeroes_to_pad = len(grid) - len(merged_elements)
        if direction == "up":
            for row in range(GRID_SIZE):
                grid[row][col] = merged_elements[row] if row < len(merged_elements) else 0
        elif direction == "down":
            for row in range(GRID_SIZE):
                grid[row][col] = 0 if row < zeroes_to_pad else merged_elements[row - zeroes_to_pad]
    return


# Resets all elements in the grid to 0 when new game button is clicked
def new_game(grid):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            grid[i][j] = 0
    add_random_tile(grid)
    return


# Checks if there is 2048 in the grid, if so return true to win
def check_win(grid):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 2048:
                return True
    return False


""" 
After prototype is finished:
    - Track the score
    - Save high scores
    - Make a proper lose screen
    - Add animations
    - Add bigger numbers
"""