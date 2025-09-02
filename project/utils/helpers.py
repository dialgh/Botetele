"""
Fonctions utilitaires pour TSUKIBOT
"""

import random
from config import NARUTO_QUOTES, NINJA_EMOJIS

def get_random_naruto_quote():
    """Retourne une citation Naruto aléatoire"""
    return random.choice(NARUTO_QUOTES)

def get_ninja_emoji():
    """Retourne un emoji ninja aléatoire"""
    return random.choice(NINJA_EMOJIS)

def format_naruto_message(title: str, content: str, emoji: str = "🍥"):
    """Formate un message avec le style Naruto"""
    return f"""
{emoji} **{title}** {emoji}

{content}

{get_random_naruto_quote()}
"""

def get_ascii_ninja():
    """Retourne l'art ASCII ninja"""
    return """
    🥷
   /|\\
   / \\
  -----
 NINJA!
"""

def is_admin_command(command: str) -> bool:
    """Vérifie si une commande nécessite des droits admin"""
    admin_commands = [
        'welcome', 'antilink', 'promote', 'promoteall', 'demote', 'demoteall',
        'kick', 'kickall', 'mute', 'unmute', 'tagadmin', 'tagall', 'groupinfo',
        'antimedia', 'antibot', 'antispam', 'antiedit', 'antiforward', 
        'antivoice', 'listusers'
    ]
    return command in admin_commands

def format_user_list(users_data):
    """Formate la liste des utilisateurs pour l'affichage"""
    if not users_data['users']:
        return "🍥 Aucun utilisateur enregistré pour le moment."
    
    message = f"👥 **LISTE DES UTILISATEURS TSUKIBOT** 👥\n\n"
    message += f"📊 Total: {users_data['total_users']} utilisateurs\n\n"
    
    for i, user in enumerate(users_data['users'], 1):
        username = user['username'] if user['username'] != "Aucun" else "Non défini"
        message += f"{i}. **{user['first_name']}**\n"
        message += f"   🆔 ID: `{user['id']}`\n"
        message += f"   👤 Username: @{username}\n"
        message += f"   📅 Premier contact: {user['first_seen'][:10]}\n\n"
    
    return message