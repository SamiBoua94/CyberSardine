"""
Gestion des mouvements de la sardine
"""
import random
from config import (
    MAX_VELOCITY, MIN_VELOCITY,
    VELOCITY_CHANGE_CHANCE, DIRECTION_CHANGE_CHANCE,
    FULL_DIRECTION_CHANGE, STATE_CHANGE_CHANCE,
    MOVE_INTERVAL
)


class MovementController:
    """Contrôleur de mouvement pour la sardine"""
    
    def __init__(self, pet):
        self.pet = pet
    
    def update(self):
        """Met à jour la position de la sardine avec mouvement aléatoire et non linéaire"""
        if not self.pet.drag_data["dragging"] and not self.pet.is_falling:
            self._apply_random_drift()
            self._apply_velocity_changes()
            self._apply_direction_changes()
            self._handle_wraparound()
            self._update_flip_direction()
            self._random_state_change()
            self._update_window_position()
        
        # Continuer le mouvement
        self.pet.window.after(MOVE_INTERVAL, self.update)
    
    def _apply_random_drift(self):
        """Ajoute des variations aléatoires pour un mouvement organique"""
        random_drift_x = random.uniform(-0.3, 0.3)
        random_drift_y = random.uniform(-0.3, 0.3)
        
        self.pet.x += self.pet.velocity_x + random_drift_x
        self.pet.y += self.pet.velocity_y + random_drift_y
    
    def _apply_velocity_changes(self):
        """Applique des changements de vitesse aléatoires"""
        if random.random() < VELOCITY_CHANGE_CHANCE:
            self.pet.velocity_x += random.uniform(-0.2, 0.2)
            self.pet.velocity_y += random.uniform(-0.2, 0.2)
            
            # Limiter les vitesses
            self.pet.velocity_x = max(MIN_VELOCITY, min(MAX_VELOCITY, self.pet.velocity_x))
            self.pet.velocity_y = max(MIN_VELOCITY, min(MAX_VELOCITY, self.pet.velocity_y))
    
    def _apply_direction_changes(self):
        """Applique des changements de direction"""
        # Changement partiel
        if random.random() < DIRECTION_CHANGE_CHANCE:
            self.pet.velocity_x += random.uniform(-0.5, 0.5)
            self.pet.velocity_y += random.uniform(-0.5, 0.5)
        
        # Changement complet
        if random.random() < FULL_DIRECTION_CHANGE:
            self.pet.velocity_x = random.uniform(-3, 3)
            self.pet.velocity_y = random.uniform(-3, 3)
    
    def _handle_wraparound(self):
        """Gère le wraparound quand la sardine sort de l'écran"""
        # Horizontal
        if self.pet.x > self.pet.screen_width:
            self.pet.x = -self.pet.sprite_width
        elif self.pet.x < -self.pet.sprite_width:
            self.pet.x = self.pet.screen_width
        
        # Vertical
        if self.pet.y > self.pet.screen_height:
            self.pet.y = -self.pet.sprite_height
        elif self.pet.y < -self.pet.sprite_height:
            self.pet.y = self.pet.screen_height
    
    def _update_flip_direction(self):
        """Met à jour la direction du flip selon le mouvement"""
        self.pet.flip = self.pet.velocity_x < 0
    
    def _random_state_change(self):
        """Change l'état aléatoirement entre swim et idle"""
        if random.random() < STATE_CHANGE_CHANCE:
            self.pet.current_state = 'idle' if self.pet.current_state == 'swim' else 'swim'
    
    def _update_window_position(self):
        """Met à jour la position de la fenêtre"""
        self.pet.window.geometry(f'+{int(self.pet.x)}+{int(self.pet.y)}')
    
    def change_direction(self):
        """Change la direction de nage de manière aléatoire"""
        self.pet.velocity_x = random.choice([2, -2, 1.5, -1.5, 3, -3])
        self.pet.velocity_y = random.choice([1.5, -1.5, 2, -2, 1, -1, 2.5, -2.5])
