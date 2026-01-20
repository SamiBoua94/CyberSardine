"""
CyberSardine - Desktop Pet
Un animal de compagnie virtuel qui se promène sur votre bureau Windows

Point d'entrée principal de l'application
"""
from sardine_pet import SardineDesktopPet


def main():
    """Fonction principale"""
    print("🐟 Lancement du Desktop Pet - CyberSardine")
    print("=" * 50)
    print("💡 Contrôles:")
    print("   • Clic gauche : Déplacer (drag)")
    print("   • Clic droit : Tuer (assiette + chute puis fermeture)")
    print("   • Double-clic : Tuer (assiette + chute, même effet)")
    print("   • Clic molette : Menu contextuel")
    print("=" * 50)
    print("🌊 La sardine nage librement sur votre écran!")
    print("🔄 Elle réapparaît de l'autre côté quand elle sort")
    print("=" * 50)
    
    pet = SardineDesktopPet()
    pet.run()


if __name__ == "__main__":
    main()
