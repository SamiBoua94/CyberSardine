# 🐟 CyberSardine - Desktop Pet

## Description
Un desktop pet interactif en forme de sardine avec des lunettes de soleil qui se promène sur votre bureau Windows! La sardine possède plusieurs animations pixel art et peut interagir avec vous.

## Contenu

### Fichiers
- **desktop_pet.py** : Application principale du desktop pet
- **generate_sprites.py** : Générateur de sprites pixélisés
- **sprites/** : Dossier contenant tous les sprites PNG
- **sardine_animation.py** : Ancienne version avec sprites ASCII
- **sardine_sprites.txt** : Visualisation des sprites ASCII

### Sprites Pixélisés

Chaque sprite est généré en pixel art avec 4 animations différentes :

1. **sardine_swim_1.png** : Position de nage 1 (queue vers le bas)
2. **sardine_swim_2.png** : Position de nage 2 (queue au milieu)
3. **sardine_swim_3.png** : Position de nage 3 (queue vers le haut)
4. **sardine_idle.png** : Position au repos

## Installation

### 1. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 2. Générer les sprites
```bash
python generate_sprites.py
```

Cela créera le dossier `sprites/` avec tous les fichiers PNG nécessaires.

### 3. Lancer le Desktop Pet
```bash
python desktop_pet.py
```

## Utilisation

### Contrôles
- **Clic gauche + glisser** : Déplacer la sardine
- **Clic droit** : Faire sauter la sardine
- **Clic molette** : Afficher le menu contextuel

### Comportements
- La sardine se déplace automatiquement de gauche à droite
- Elle rebondit sur les bords de l'écran
- Elle alterne entre animation de nage et position repos
- Transparent et toujours au premier plan

## Caractéristiques
- 🕶️ Lunettes de soleil stylées en pixel art
- 🌊 Animations de nage fluides
- 🎨 Sprites en pixel art colorés (32x24 pixels)
- 🖱️ Interactif (déplaçable, peut sauter)
- 💨 Transparent, se promène sur votre bureau
- ⚡ Léger et amusant

## Personnalisation

### Dans `generate_sprites.py`
- `PIXEL_SIZE` : Taille de chaque pixel (défaut: 4)
- Couleurs : Modifiez les variables de couleur pour changer l'apparence
- Dessins : Créez vos propres sprites en modifiant les grilles

### Dans `desktop_pet.py`
- `velocity_x` : Vitesse de déplacement horizontal
- `animation_speed` : Vitesse d'animation (en millisecondes)
- `gravity` : Force de gravité pour les sauts

## Requis
- Python 3.x
- Pillow (PIL) - Pour la génération et l'affichage des sprites
- tkinter - Inclus avec Python pour l'interface graphique
