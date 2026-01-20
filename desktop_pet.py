"""
Desktop Pet - Sardine avec lunettes de soleil
Un animal de compagnie qui se promène sur votre bureau Windows
"""
import tkinter as tk
from PIL import Image, ImageTk
import random
import os

class SardineDesktopPet:
    def __init__(self):
        # Créer la fenêtre principale
        self.window = tk.Tk()
        self.window.title("CyberSardine")
        
        # Rendre la fenêtre transparente et toujours au premier plan
        self.window.attributes('-transparentcolor', 'white')
        self.window.attributes('-topmost', True)
        self.window.overrideredirect(True)  # Enlever les bordures de fenêtre
        
        # Position et vitesse
        self.x = 500
        self.y = 500
        self.velocity_x = random.choice([2, -2])  # Mouvement horizontal aléatoire
        self.velocity_y = random.choice([1.5, -1.5])  # Mouvement vertical aléatoire
        self.sprite_width = 128  # Largeur du sprite
        self.sprite_height = 96  # Hauteur du sprite
        
        # État de l'animation
        self.current_state = 'swim'
        self.animation_frame = 0
        self.animation_speed = 200  # ms entre chaque frame
        self.flip = False  # Direction (False = droite, True = gauche)
        
        # Charger les sprites
        self.sprites = self.load_sprites()
        
        # Label pour afficher le sprite
        self.label = tk.Label(self.window, bg='white')
        self.label.pack()
        
        # Permettre de déplacer la fenêtre
        self.label.bind('<Button-1>', self.start_drag)
        self.label.bind('<B1-Motion>', self.drag)
        self.label.bind('<ButtonRelease-1>', self.stop_drag)
        self.label.bind('<Button-3>', self.change_direction)  # Clic droit pour changer de direction
        
        # Variables pour le drag
        self.drag_data = {"x": 0, "y": 0, "dragging": False}
        
        # Menu contextuel
        self.create_context_menu()
        
        # Dimensions de l'écran
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        
        # Démarrer l'animation
        self.update_animation()
        self.move()
        
    def load_sprites(self):
        """Charge tous les sprites depuis le dossier sprites/"""
        sprites = {
            'swim': [],
            'idle': None
        }
        
        sprite_dir = 'sprites'
        
        # Charger les sprites de nage
        for i in range(1, 4):
            try:
                img = Image.open(f'{sprite_dir}/sardine_swim_{i}.png')
                sprites['swim'].append(ImageTk.PhotoImage(img))
            except:
                print(f"Erreur: sprite sardine_swim_{i}.png non trouvé")
        
        # Charger le sprite idle
        try:
            img = Image.open(f'{sprite_dir}/sardine_idle.png')
            sprites['idle'] = ImageTk.PhotoImage(img)
        except:
            print(f"Erreur: sprite sardine_idle.png non trouvé")
        
        return sprites
    
    def update_animation(self):
        """Met à jour le sprite affiché"""
        if self.current_state == 'swim' and self.sprites['swim']:
            # Animation de nage - cycle entre les 3 sprites
            sprite = self.sprites['swim'][self.animation_frame % len(self.sprites['swim'])]
            
            self.label.config(image=sprite)
            self.animation_frame += 1
            
        elif self.current_state == 'idle' and self.sprites['idle']:
            self.label.config(image=self.sprites['idle'])
        
        # Continuer l'animation
        self.window.after(self.animation_speed, self.update_animation)
    
    def move(self):
        """Déplace la sardine sur l'écran avec mouvement aléatoire et non linéaire"""
        if not self.drag_data["dragging"]:
            # Ajouter des variations aléatoires à chaque frame pour un mouvement organique
            random_drift_x = random.uniform(-0.3, 0.3)
            random_drift_y = random.uniform(-0.3, 0.3)
            
            # Appliquer le mouvement avec variation aléatoire
            self.x += self.velocity_x + random_drift_x
            self.y += self.velocity_y + random_drift_y
            
            # Variation aléatoire de la vitesse pour un mouvement non linéaire
            if random.random() < 0.1:  # 10% de chance de modifier légèrement la vitesse
                self.velocity_x += random.uniform(-0.2, 0.2)
                self.velocity_y += random.uniform(-0.2, 0.2)
                
                # Limiter les vitesses pour éviter qu'elle n'aille trop vite
                self.velocity_x = max(-4, min(4, self.velocity_x))
                self.velocity_y = max(-4, min(4, self.velocity_y))
            
            # Changement de direction plus fréquent et progressif
            if random.random() < 0.02:  # 2% de chance de changer partiellement la direction
                angle_change = random.uniform(-0.5, 0.5)
                self.velocity_x += angle_change
                self.velocity_y += random.uniform(-0.5, 0.5)
            
            # Changement de direction complet moins fréquent
            if random.random() < 0.008:  # 0.8% de chance de changer complètement de direction
                self.velocity_x = random.uniform(-3, 3)
                self.velocity_y = random.uniform(-3, 3)
            
            # Wraparound horizontal : si sort à droite, réapparaît à gauche
            if self.x > self.screen_width:
                self.x = -self.sprite_width
            elif self.x < -self.sprite_width:
                self.x = self.screen_width
            
            # Wraparound vertical : si sort en haut, réapparaît en bas
            if self.y > self.screen_height:
                self.y = -self.sprite_height
            elif self.y < -self.sprite_height:
                self.y = self.screen_height
            
            # Changer la direction du flip selon la direction horizontale
            self.flip = self.velocity_x < 0
            
            # Changer d'état aléatoirement
            if random.random() < 0.01:  # 1% de chance à chaque frame
                self.current_state = 'idle' if self.current_state == 'swim' else 'swim'
            
            # Mettre à jour la position de la fenêtre
            self.window.geometry(f'+{int(self.x)}+{int(self.y)}')
        
        # Continuer le mouvement
        self.window.after(50, self.move)
    
    def change_direction(self, event=None):
        """Change la direction de nage de la sardine"""
        self.velocity_x = random.choice([2, -2, 1.5, -1.5, 3, -3])
        self.velocity_y = random.choice([1.5, -1.5, 2, -2, 1, -1, 2.5, -2.5])
    
    def start_drag(self, event):
        """Commence à déplacer la sardine"""
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y
        self.drag_data["dragging"] = True
        self.current_state = 'idle'
    
    def drag(self, event):
        """Déplace la sardine avec la souris"""
        if self.drag_data["dragging"]:
            delta_x = event.x - self.drag_data["x"]
            delta_y = event.y - self.drag_data["y"]
            self.x = self.window.winfo_x() + delta_x
            self.y = self.window.winfo_y() + delta_y
            self.window.geometry(f'+{int(self.x)}+{int(self.y)}')
    
    def stop_drag(self, event):
        """Arrête le déplacement"""
        self.drag_data["dragging"] = False
        self.current_state = 'swim'
    
    def create_context_menu(self):
        """Crée le menu contextuel"""
        self.context_menu = tk.Menu(self.window, tearoff=0)
        self.context_menu.add_command(label="🐟 Changer de direction", command=self.change_direction)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="❌ Quitter", command=self.quit_app)
        
        self.label.bind('<Button-2>', self.show_context_menu)  # Clic molette
    
    def show_context_menu(self, event):
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

if __name__ == "__main__":
    print("🐟 Lancement du Desktop Pet - CyberSardine")
    print("💡 Conseils:")
    print("   - Clic gauche + glisser pour déplacer")
    print("   - Clic droit pour changer de direction")
    print("   - Clic molette pour le menu")
    print("   - La sardine se déplace dans toutes les directions")
    print("   - Elle réapparaît de l'autre côté quand elle sort de l'écran")
    
    pet = SardineDesktopPet()
    pet.run()
