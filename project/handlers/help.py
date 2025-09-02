"""
Handlers pour les commandes d'aide
"""

from telegram import Update
from telegram.ext import ContextTypes
from utils.helpers import format_naruto_message, get_ascii_ninja
from config import BOT_NAME, OWNER_USERNAME, MAIN_MENU

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /help"""
    help_text = f"""
{MAIN_MENU}

🍥 **COMMENT UTILISER TSUKIBOT** 🍥

📋 **Commandes générales** - Utilisables par tous
🎭 **Commandes médias** - Recherche et gestion
💾 **Commandes stockage** - Sauvegarde personnelle
⚔️ **Commandes admin** - Réservées aux admins
🎮 **Divertissement** - Fun et motivation
❓ **Aide** - Support et documentation

🥷 *Tapez une commande pour l'essayer!*
"""
    
    await update.message.reply_text(help_text, parse_mode='Markdown')

async def doc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /doc"""
    doc_text = f"""
📚 **DOCUMENTATION TSUKIBOT** 📚

🔰 **GUIDE DÉMARRAGE RAPIDE**
1. Utilisez `/start` pour voir le menu principal
2. Choisissez une catégorie de commandes
3. Tapez la commande désirée
4. Suivez les instructions ninja!

🛠️ **FONCTIONNALITÉS PRINCIPALES**
• Gestion complète de groupe
• Stockage de médias personnel
• Protection anti-spam/liens
• Divertissement avec thème Naruto
• Tracking des utilisateurs

⚙️ **PERMISSIONS REQUISES**
• Commandes générales: Aucune
• Commandes admin: Droits administrateur
• Commandes owner: Propriétaire uniquement

🎯 **SUPPORT TECHNIQUE**
Contact: {OWNER_USERNAME}

{get_ascii_ninja()}
"""
    
    await update.message.reply_text(doc_text, parse_mode='Markdown')

async def updates_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /updates"""
    updates_text = format_naruto_message(
        "MISES À JOUR NINJA",
        """
🆕 **VERSION 1.0.0** (Actuelle)
• Lancement initial de TSUKIBOT
• Menu complet avec thème Naruto
• Système de tracking utilisateurs
• Commandes de base implémentées
• Protection de groupe basique

🔮 **PROCHAINES MISES À JOUR**
• Intégration API médias externes
• Système de points ninja
• Mini-jeux Naruto
• Stickers personnalisés
• Base de données avancée

📅 Dernière mise à jour: Janvier 2025
""",
        "🆕"
    )
    
    await update.message.reply_text(updates_text, parse_mode='Markdown')

async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /about"""
    about_text = f"""
🍥 **À PROPOS DE TSUKIBOT** 🍥

🤖 **Nom**: {BOT_NAME}
👨‍💻 **Créateur**: {OWNER_USERNAME}
🎭 **Thème**: Naruto Uzumaki
📅 **Version**: 1.0.0
🏗️ **Framework**: python-telegram-bot

🎯 **MISSION**
Créer un assistant Telegram inspiré de l'univers Naruto pour aider les utilisateurs dans leurs groupes avec style et efficacité!

🥷 **PHILOSOPHIE**
"Un ninja ne recule jamais devant ses mots, c'est sa voie ninja!" - Naruto

💝 **REMERCIEMENTS**
Merci à tous les utilisateurs ninja qui font vivre ce bot!

{get_ascii_ninja()}

🍥 *Dattebayo!* 🍥
"""
    
    await update.message.reply_text(about_text, parse_mode='Markdown')