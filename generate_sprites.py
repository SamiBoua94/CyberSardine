"""
Générateur de sprites pixélisés pour la sardine avec lunettes de soleil
"""
from PIL import Image, ImageDraw

# Taille d'un pixel (pour agrandir le sprite)
PIXEL_SIZE = 4
SPRITE_WIDTH = 32
SPRITE_HEIGHT = 24

# Couleurs
TRANSPARENT = (0, 0, 0, 0)
BLUE = (70, 130, 220, 255)        # Corps de la sardine
DARK_BLUE = (40, 80, 150, 255)    # Contour
SILVER = (192, 192, 192, 255)     # Reflets
WHITE = (255, 255, 255, 255)      # Yeux
BLACK = (0, 0, 0, 255)            # Lunettes
GRAY = (100, 100, 100, 255)       # Monture des lunettes
YELLOW = (255, 215, 0, 255)       # Détails dorés
RED = (220, 50, 50, 255)          # Nageoires

def create_pixel_grid(width, height):
    """Crée une grille de pixels transparente"""
    return [[TRANSPARENT for _ in range(width)] for _ in range(height)]

def draw_sardine_swim_1():
    """Sprite de la sardine - Position de nage 1 (queue vers le bas)"""
    grid = create_pixel_grid(SPRITE_WIDTH, SPRITE_HEIGHT)
    
    # Queue (position basse)
    for i in range(3):
        grid[18+i][2] = RED
        grid[18+i][3] = RED
    
    # Corps principal
    for y in range(8, 17):
        for x in range(5, 25):
            grid[y][x] = BLUE
    
    # Contour sombre
    for x in range(5, 25):
        grid[7][x] = DARK_BLUE
        grid[16][x] = DARK_BLUE
    for y in range(8, 16):
        grid[y][5] = DARK_BLUE
        grid[y][24] = DARK_BLUE
    
    # Tête ronde
    grid[7][6] = DARK_BLUE
    grid[7][7] = BLUE
    grid[16][6] = DARK_BLUE
    grid[16][7] = BLUE
    
    # Lunettes de soleil (verres noirs)
    grid[10][8] = GRAY
    grid[10][9] = BLACK
    grid[10][10] = BLACK
    grid[10][11] = GRAY
    grid[11][8] = BLACK
    grid[11][9] = BLACK
    grid[11][10] = BLACK
    grid[11][11] = BLACK
    
    grid[10][13] = GRAY
    grid[10][14] = BLACK
    grid[10][15] = BLACK
    grid[10][16] = GRAY
    grid[11][13] = BLACK
    grid[11][14] = BLACK
    grid[11][15] = BLACK
    grid[11][16] = BLACK
    
    # Pont entre les lunettes
    grid[10][12] = GRAY
    grid[11][12] = GRAY
    
    # Reflets argentés sur le corps
    for x in range(8, 23, 3):
        grid[9][x] = SILVER
        grid[14][x] = SILVER
    
    # Queue détaillée
    grid[17][3] = DARK_BLUE
    grid[17][4] = RED
    grid[18][4] = RED
    grid[19][3] = DARK_BLUE
    
    # Nageoire dorsale
    grid[6][15] = RED
    grid[6][16] = RED
    grid[7][15] = RED
    
    return grid

def draw_sardine_swim_2():
    """Sprite de la sardine - Position de nage 2 (queue au milieu)"""
    grid = create_pixel_grid(SPRITE_WIDTH, SPRITE_HEIGHT)
    
    # Queue (position milieu)
    for i in range(3):
        grid[11+i][2] = RED
        grid[11+i][3] = RED
    
    # Corps principal
    for y in range(8, 17):
        for x in range(5, 25):
            grid[y][x] = BLUE
    
    # Contour sombre
    for x in range(5, 25):
        grid[7][x] = DARK_BLUE
        grid[16][x] = DARK_BLUE
    for y in range(8, 16):
        grid[y][5] = DARK_BLUE
        grid[y][24] = DARK_BLUE
    
    # Tête ronde
    grid[7][6] = DARK_BLUE
    grid[7][7] = BLUE
    grid[16][6] = DARK_BLUE
    grid[16][7] = BLUE
    
    # Lunettes de soleil
    grid[10][8] = GRAY
    grid[10][9] = BLACK
    grid[10][10] = BLACK
    grid[10][11] = GRAY
    grid[11][8] = BLACK
    grid[11][9] = BLACK
    grid[11][10] = BLACK
    grid[11][11] = BLACK
    
    grid[10][13] = GRAY
    grid[10][14] = BLACK
    grid[10][15] = BLACK
    grid[10][16] = GRAY
    grid[11][13] = BLACK
    grid[11][14] = BLACK
    grid[11][15] = BLACK
    grid[11][16] = BLACK
    
    grid[10][12] = GRAY
    grid[11][12] = GRAY
    
    # Reflets argentés
    for x in range(8, 23, 3):
        grid[9][x] = SILVER
        grid[14][x] = SILVER
    
    # Queue détaillée
    grid[11][3] = DARK_BLUE
    grid[11][4] = RED
    grid[12][4] = RED
    grid[13][3] = DARK_BLUE
    
    # Nageoire dorsale
    grid[6][15] = RED
    grid[6][16] = RED
    grid[7][15] = RED
    
    return grid

def draw_sardine_swim_3():
    """Sprite de la sardine - Position de nage 3 (queue vers le haut)"""
    grid = create_pixel_grid(SPRITE_WIDTH, SPRITE_HEIGHT)
    
    # Queue (position haute)
    for i in range(3):
        grid[4+i][2] = RED
        grid[4+i][3] = RED
    
    # Corps principal
    for y in range(8, 17):
        for x in range(5, 25):
            grid[y][x] = BLUE
    
    # Contour sombre
    for x in range(5, 25):
        grid[7][x] = DARK_BLUE
        grid[16][x] = DARK_BLUE
    for y in range(8, 16):
        grid[y][5] = DARK_BLUE
        grid[y][24] = DARK_BLUE
    
    # Tête ronde
    grid[7][6] = DARK_BLUE
    grid[7][7] = BLUE
    grid[16][6] = DARK_BLUE
    grid[16][7] = BLUE
    
    # Lunettes de soleil
    grid[10][8] = GRAY
    grid[10][9] = BLACK
    grid[10][10] = BLACK
    grid[10][11] = GRAY
    grid[11][8] = BLACK
    grid[11][9] = BLACK
    grid[11][10] = BLACK
    grid[11][11] = BLACK
    
    grid[10][13] = GRAY
    grid[10][14] = BLACK
    grid[10][15] = BLACK
    grid[10][16] = GRAY
    grid[11][13] = BLACK
    grid[11][14] = BLACK
    grid[11][15] = BLACK
    grid[11][16] = BLACK
    
    grid[10][12] = GRAY
    grid[11][12] = GRAY
    
    # Reflets argentés
    for x in range(8, 23, 3):
        grid[9][x] = SILVER
        grid[14][x] = SILVER
    
    # Queue détaillée
    grid[5][3] = DARK_BLUE
    grid[5][4] = RED
    grid[6][4] = RED
    grid[7][3] = DARK_BLUE
    
    # Nageoire dorsale
    grid[6][15] = RED
    grid[6][16] = RED
    grid[7][15] = RED
    
    return grid

def draw_sardine_idle():
    """Sprite de la sardine - Position idle (repos)"""
    grid = create_pixel_grid(SPRITE_WIDTH, SPRITE_HEIGHT)
    
    # Queue (position normale)
    for i in range(4):
        grid[10+i][2] = RED
        grid[10+i][3] = RED
    grid[11][1] = RED
    grid[12][1] = RED
    
    # Corps principal
    for y in range(8, 17):
        for x in range(5, 25):
            grid[y][x] = BLUE
    
    # Contour sombre
    for x in range(5, 25):
        grid[7][x] = DARK_BLUE
        grid[16][x] = DARK_BLUE
    for y in range(8, 16):
        grid[y][5] = DARK_BLUE
        grid[y][24] = DARK_BLUE
    
    # Tête ronde
    grid[7][6] = DARK_BLUE
    grid[7][7] = BLUE
    grid[16][6] = DARK_BLUE
    grid[16][7] = BLUE
    
    # Lunettes de soleil
    grid[10][8] = GRAY
    grid[10][9] = BLACK
    grid[10][10] = BLACK
    grid[10][11] = GRAY
    grid[11][8] = BLACK
    grid[11][9] = BLACK
    grid[11][10] = BLACK
    grid[11][11] = BLACK
    
    grid[10][13] = GRAY
    grid[10][14] = BLACK
    grid[10][15] = BLACK
    grid[10][16] = GRAY
    grid[11][13] = BLACK
    grid[11][14] = BLACK
    grid[11][15] = BLACK
    grid[11][16] = BLACK
    
    grid[10][12] = GRAY
    grid[11][12] = GRAY
    
    # Reflets argentés
    for x in range(8, 23, 3):
        grid[9][x] = SILVER
        grid[14][x] = SILVER
    
    # Nageoire dorsale
    grid[6][15] = RED
    grid[6][16] = RED
    grid[7][15] = RED
    
    # Nageoire ventrale
    grid[17][12] = RED
    grid[17][13] = RED
    
    return grid

def grid_to_image(grid):
    """Convertit une grille de pixels en image PIL"""
    img = Image.new('RGBA', (SPRITE_WIDTH * PIXEL_SIZE, SPRITE_HEIGHT * PIXEL_SIZE), TRANSPARENT)
    draw = ImageDraw.Draw(img)
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != TRANSPARENT:
                x_pos = x * PIXEL_SIZE
                y_pos = y * PIXEL_SIZE
                draw.rectangle(
                    [x_pos, y_pos, x_pos + PIXEL_SIZE - 1, y_pos + PIXEL_SIZE - 1],
                    fill=grid[y][x]
                )
    
    return img

def generate_all_sprites():
    """Génère tous les sprites et les sauvegarde"""
    sprites = {
        'sardine_swim_1.png': draw_sardine_swim_1(),
        'sardine_swim_2.png': draw_sardine_swim_2(),
        'sardine_swim_3.png': draw_sardine_swim_3(),
        'sardine_idle.png': draw_sardine_idle(),
    }
    
    for filename, grid in sprites.items():
        img = grid_to_image(grid)
        img.save(f'sprites/{filename}')
        print(f"✓ Sprite créé: {filename}")
    
    print(f"\n🐟 {len(sprites)} sprites générés avec succès!")

if __name__ == "__main__":
    import os
    os.makedirs('sprites', exist_ok=True)
    generate_all_sprites()
