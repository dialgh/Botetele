"""
Configuration du bot TSUKIBOT
"""

# Informations du bot
BOT_TOKEN = "7630392456:AAF1zCaUxXoQZlZFZQWYXe5PNuzcJxni7mE"
OWNER_ID = 6327576602
OWNER_USERNAME = "@jeff_mitsuki"
BOT_NAME = "TSUKIBOT"

# Fichiers de données
USERS_FILE = "data/users.json"
SETTINGS_FILE = "data/settings.json"

# Citations Naruto
NARUTO_QUOTES = [
    "Dattebayo! Je ne recule jamais devant mes mots, c'est ma voie ninja! 🍥",
    "Un ninja ne doit jamais abandonner! 🥷",
    "Crois en toi-même et tu pourras tout accomplir! ⚡",
    "La vraie force vient du fait de protéger ce qui t'est cher! 💪",
    "Je vais devenir Hokage, dattebayo! 🔥",
    "Les amis sont les plus précieux des trésors! 👥",
    "Un shinobi doit voir au-delà de ce qui se cache sous les apparences! 👁️",
    "L'erreur n'est humaine que si l'on cherche à s'améliorer! 📈"
]

# Emojis thématiques
NINJA_EMOJIS = ["🥷", "⚡", "🔥", "🍥", "🌀", "⚔️", "🎯", "💨"]

# Messages de bienvenue
WELCOME_BANNER = """
╔══════════════════════════════════════╗
║  🍥    TSUKIBOT - NINJA ASSISTANT   🍥  ║
║              Thème Naruto             ║
║         Par @jeff_mitsuki            ║
╚══════════════════════════════════════╝
"""

MAIN_MENU = """
🥷 **MENU PRINCIPAL TSUKIBOT** 🥷

┌─「 📋 GÉNÉRAL 」
├ /ping - Vérifier le statut
├ /date - Date et heure actuelles
├ /contact - Contacter le développeur
├ /info - Informations utilisateur
└ /quote - Citation Naruto aléatoire

┌─「 🎭 MÉDIAS 」
├ /img - Rechercher images
├ /gif - Rechercher GIFs
├ /stk - Créer sticker
└ /vu - Générer vue temporaire

┌─「 💾 STOCKAGE 」
├ /store - Stocker média
├ /list - Lister médias stockés
└ /delmedia - Supprimer média

┌─「 ⚔️ ADMINISTRATION 」
├ /welcome - Configurer message bienvenue
├ /antilink - Protection anti-liens
├ /promote - Promouvoir membre
├ /kick - Expulser membre
├ /mute - Rendre muet
└ /listusers - Lister utilisateurs (Owner)

┌─「 🎮 DIVERTISSEMENT 」
├ /motivation - Message motivant
├ /youtube - Rechercher vidéos
└ /tiktok - Rechercher TikTok

┌─「 ❓ AIDE 」
├ /help - Aide détaillée
├ /doc - Documentation
└ /about - À propos du bot

🍥 *"Crois en ton potentiel ninja!"* - Naruto
"""