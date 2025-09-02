"""
Script de lancement simple pour TSUKIBOT
"""

import sys
import os

def main():
    """Lancement du bot avec vérifications"""
    print("🍥 Démarrage de TSUKIBOT...")
    print("🥷 Vérification des dépendances...")
    
    try:
        import telegram
        print("✅ python-telegram-bot trouvé")
    except ImportError:
        print("❌ python-telegram-bot manquant!")
        print("💡 Installez avec: pip install -r requirements.txt")
        sys.exit(1)
    
    # Vérifier la structure des dossiers
    required_dirs = ['data', 'logs', 'media', 'handlers', 'utils']
    for dir_name in required_dirs:
        if not os.path.exists(dir_name):
            print(f"📁 Création du dossier: {dir_name}")
            os.makedirs(dir_name, exist_ok=True)
    
    print("🚀 Lancement du bot...")
    
    # Importer et lancer le bot
    from bot import main as bot_main
    bot_main()

if __name__ == '__main__':
    main()