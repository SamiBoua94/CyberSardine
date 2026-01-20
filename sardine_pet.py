"""
Classe principale du Desktop Pet - Sardine avec lunettes de soleil
"""
import tkinter as tk
import random

from config import (
    SPRITE_WIDTH, SPRITE_HEIGHT,
    INITIAL_VELOCITY_X, INITIAL_VELOCITY_Y
)
from sprites_loader import load_all_sprites
from movement import MovementController
from animation import AnimationController
from actions import ActionsController


class SardineDesktopPet:
    """Desktop Pet - Une sardine avec lunettes de soleil"""
    
    def __init__(self):
        # Créer la fenêtre principale
        self.window = tk.Tk()
        self.window.title("CyberSardine")
        
        # Rendre la fenêtre transparente et toujours au premier plan
        self.window.attributes('-transparentcolor', 'white')
        self.window.attributes('-topmost', True)
        self.window.overrideredirect(True)
        
        # Position et vitesse
        self.x = 500
        self.y = 500
        self.velocity_x = random.choice(INITIAL_VELOCITY_X)
        self.velocity_y = random.choice(INITIAL_VELOCITY_Y)
        self.sprite_width = SPRITE_WIDTH
        self.sprite_height = SPRITE_HEIGHT
        
        # État
        self.current_state = 'swim'
        self.flip = False
        self.is_falling = False
        self.is_dead = False
        self.drag_data = {"x": 0, "y": 0, "dragging": False}
        
        # Dimensions de l'écran
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        
        # Charger les sprites
        self.sprites = load_all_sprites()
        
        # Créer le label pour afficher le sprite
        self.label = tk.Label(self.window, bg='white')
        self.label.pack()
        
        # Initialiser les contrôleurs
        self.movement = MovementController(self)
        self.animation = AnimationController(self)
        self.actions = ActionsController(self)
        
        # Configurer les événements
        self._setup_bindings()
        self._create_context_menu()
        
        # Démarrer l'animation et le mouvement
        self.animation.update()
        self.movement.update()
    
    def _setup_bindings(self):
        """Configure les événements de la souris"""
        # Clic gauche: drag pour déplacer
        self.label.bind('<Button-1>', self.actions.start_drag)
        self.label.bind('<B1-Motion>', self.actions.drag)
        self.label.bind('<ButtonRelease-1>', self.actions.stop_drag)
        # Double-clic: kill (assiette + chute)
        self.label.bind('<Double-Button-1>', self.actions.transform_and_quit)
        # Clic droit: kill (assiette + chute)
        self.label.bind('<Button-3>', self.actions.click_transform_fall)
    
    def _create_context_menu(self):
        """Crée le menu contextuel"""
        self.context_menu = tk.Menu(self.window, tearoff=0)
        self.context_menu.add_command(
            label="🐟 Changer de direction",
            command=self.movement.change_direction
        )
        self.context_menu.add_separator()
        self.context_menu.add_command(
            label="❌ Quitter",
            command=self.quit_app
        )
        
        self.label.bind('<Button-2>', self._show_context_menu)
    
    def _show_context_menu(self, event):
        """Affiche le menu contextuel"""
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()
    
    def quit_app(self):
        """Ferme l'application"""
        self.window.quit()
    
    def run(self):
        """Lance l'application"""
        self.window.mainloop()
