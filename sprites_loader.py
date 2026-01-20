"""
Gestion des sprites pour CyberSardine Desktop Pet
"""
from PIL import Image, ImageTk
from config import SPRITE_DIR


def load_all_sprites():
    """Charge tous les sprites depuis le dossier sprites/"""
    sprites = {
        'swim': [],
        'swim_flipped': [],
        'idle': None,
        'idle_flipped': None
    }
    
    # Charger les sprites de nage
    for i in range(1, 4):
        try:
            img = Image.open(f'{SPRITE_DIR}/sardine_swim_{i}.png')
            # Version normale (va vers la droite)
            sprites['swim'].append(ImageTk.PhotoImage(img))
            # Version inversée (va vers la gauche)
            img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
            sprites['swim_flipped'].append(ImageTk.PhotoImage(img_flipped))
        except Exception as e:
            print(f"Erreur: sprite sardine_swim_{i}.png non trouvé - {e}")
    
    # Charger le sprite idle
    try:
        img = Image.open(f'{SPRITE_DIR}/sardine_idle.png')
        sprites['idle'] = ImageTk.PhotoImage(img)
        # Version inversée
        img_flipped = img.transpose(Image.FLIP_LEFT_RIGHT)
        sprites['idle_flipped'] = ImageTk.PhotoImage(img_flipped)
    except Exception as e:
        print(f"Erreur: sprite sardine_idle.png non trouvé - {e}")
    
    return sprites
