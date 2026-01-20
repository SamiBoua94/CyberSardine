"""
Gestion de l'animation de la sardine
"""
from config import ANIMATION_SPEED


class AnimationController:
    """Contrôleur d'animation pour la sardine"""
    
    def __init__(self, pet):
        self.pet = pet
        self.frame = 0
    
    def update(self):
        """Met à jour le sprite affiché selon la direction"""
        # Ne rien changer si le poisson est "mort" (assiette), pour ne pas écraser le sprite
        if getattr(self.pet, 'is_dead', False):
            self.pet.window.after(ANIMATION_SPEED, self.update)
            return

        if self.pet.current_state == 'swim' and self.pet.sprites['swim']:
            self._update_swim_animation()
        elif self.pet.current_state == 'idle':
            self._update_idle_animation()
        
        # Continuer l'animation
        self.pet.window.after(ANIMATION_SPEED, self.update)
    
    def _update_swim_animation(self):
        """Met à jour l'animation de nage"""
        # Choisir le bon set de sprites selon la direction horizontale
        if self.pet.velocity_x >= 0:
            sprite_list = self.pet.sprites['swim']
        else:
            sprite_list = self.pet.sprites['swim_flipped']
        
        # Cycle entre les sprites
        sprite = sprite_list[self.frame % len(sprite_list)]
        self.pet.label.config(image=sprite)
        self.frame += 1
    
    def _update_idle_animation(self):
        """Met à jour l'animation idle"""
        if self.pet.velocity_x >= 0:
            self.pet.label.config(image=self.pet.sprites['idle'])
        else:
            self.pet.label.config(image=self.pet.sprites['idle_flipped'])
