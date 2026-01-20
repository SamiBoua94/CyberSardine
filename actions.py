"""
Gestion des actions spéciales (chute, drag, etc.)
"""
import random
from config import FALL_SPEED, FALL_ANIMATION_INTERVAL, WAIT_BEFORE_QUIT


class ActionsController:
    """Contrôleur d'actions spéciales pour la sardine"""
    
    def __init__(self, pet):
        self.pet = pet
    
    def start_fall(self, event=None):
        """Le poisson tombe vers le bas de l'écran"""
        if not self.pet.is_falling:
            self.pet.is_falling = True
            self.pet.current_state = 'idle'
            self._animate_fall()

    def click_transform_fall(self, event=None):
        """Transforme immédiatement en assiette puis tombe jusqu'en bas, puis quitte."""
        if self.pet.is_dead or self.pet.is_falling:
            return
        # Marquer comme 'dead' pour arrêter le mouvement
        self.pet.is_dead = True
        self.pet.is_falling = True
        # Changer l'image en assiette immédiatement
        if self.pet.sprites.get('plate'):
            self.pet.label.config(image=self.pet.sprites['plate'])
        # Lancer la chute
        self._animate_fall()
    
    def _animate_fall(self):
        """Animation de la chute du poisson"""
        if not self.pet.is_falling:
            return
        
        # Calculer le bas de l'écran
        bottom = self.pet.screen_height - self.pet.sprite_height - 50
        
        # Tomber jusqu'en bas
        if self.pet.y < bottom:
            self.pet.y += FALL_SPEED
            self.pet.window.geometry(f'+{int(self.pet.x)}+{int(self.pet.y)}')
            self.pet.window.after(FALL_ANIMATION_INTERVAL, self._animate_fall)
        else:
            # Arrivé en bas - rester en assiette si déjà transformé, sinon transformer
            self.pet.y = bottom
            self.pet.window.geometry(f'+{int(self.pet.x)}+{int(self.pet.y)}')
            if not self.pet.is_dead:
                self._transform_to_plate()
                self.pet.is_dead = True
            # Attendre puis quitter
            self.pet.window.after(WAIT_BEFORE_QUIT, self.pet.quit_app)
    
    def _transform_to_plate(self):
        """Transforme le poisson en assiette"""
        if self.pet.sprites['plate']:
            self.pet.label.config(image=self.pet.sprites['plate'])
            # L'attente/fermeture est gérée par l'appelant
    
    def start_drag(self, event):
        """Commence à déplacer la sardine"""
        self.pet.drag_data["x"] = event.x
        self.pet.drag_data["y"] = event.y
        self.pet.drag_data["dragging"] = True
        self.pet.current_state = 'idle'
    
    def drag(self, event):
        """Déplace la sardine avec la souris"""
        if self.pet.drag_data["dragging"]:
            delta_x = event.x - self.pet.drag_data["x"]
            delta_y = event.y - self.pet.drag_data["y"]
            self.pet.x = self.pet.window.winfo_x() + delta_x
            self.pet.y = self.pet.window.winfo_y() + delta_y
            self.pet.window.geometry(f'+{int(self.pet.x)}+{int(self.pet.y)}')
    
    def stop_drag(self, event):
        """Arrête le déplacement"""
        self.pet.drag_data["dragging"] = False
        self.pet.current_state = 'swim'
    
    def transform_and_quit(self, event=None):
        """Double-clic : utiliser le même flux que le clic simple (assiette + chute)."""
        self.click_transform_fall(event)
    
    def respawn(self):
        """Fait réapparaître le poisson ailleurs"""
        self.pet.is_falling = False
        self.pet.current_state = 'swim'
        self.pet.x = random.randint(100, self.pet.screen_width - 200)
        self.pet.y = random.randint(100, self.pet.screen_height - 300)
        self.pet.velocity_x = random.choice([2, -2, 1.5, -1.5])
        self.pet.velocity_y = random.choice([1.5, -1.5, 2, -2])
        self.pet.window.geometry(f'+{int(self.pet.x)}+{int(self.pet.y)}')
