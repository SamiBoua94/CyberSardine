"""
Configuration et constantes pour CyberSardine Desktop Pet
"""

# Dimensions du sprite
SPRITE_WIDTH = 128
SPRITE_HEIGHT = 96

# Animation
ANIMATION_SPEED = 200  # ms entre chaque frame
MOVE_INTERVAL = 50     # ms entre chaque mise à jour de position

# Vitesses de déplacement
INITIAL_VELOCITY_X = [2, -2]
INITIAL_VELOCITY_Y = [1.5, -1.5]
MAX_VELOCITY = 4
MIN_VELOCITY = -4

# Probabilités de changement
VELOCITY_CHANGE_CHANCE = 0.1      # 10% de chance de modifier la vitesse
DIRECTION_CHANGE_CHANCE = 0.02    # 2% de chance de changer partiellement la direction
FULL_DIRECTION_CHANGE = 0.008     # 0.8% de chance de changer complètement
STATE_CHANGE_CHANCE = 0.01        # 1% de chance de changer d'état (swim/idle)

# Chute
FALL_SPEED = 15
FALL_ANIMATION_INTERVAL = 30  # ms
WAIT_BEFORE_QUIT = 10000  # ms (10 secondes en bas avant de quitter)

# Dossier des sprites
SPRITE_DIR = 'sprites'
