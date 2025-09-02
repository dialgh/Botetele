"""
Handlers pour les commandes de divertissement
"""

from telegram import Update
from telegram.ext import ContextTypes
import random
from utils.helpers import format_naruto_message, get_ninja_emoji

MOTIVATION_MESSAGES = [
    "💪 Tu as la force d'un ninja légendaire en toi!",
    "🔥 Chaque échec est une leçon vers la réussite!",
    "⚡ Ton potentiel ninja n'a pas de limites!",
    "🌟 Crois en toi comme Naruto croit en ses amis!",
    "🎯 Concentre ton chakra et atteins tes objectifs!",
    "🚀 Tu es capable de devenir le hokage de ta propre vie!",
    "💎 Chaque difficulté forge un ninja plus fort!",
    "🌈 Après la tempête vient toujours l'arc-en-ciel!"
]

async def motivation_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /motivation"""
    motivation = random.choice(MOTIVATION_MESSAGES)
    user = update.effective_user
    
    message = format_naruto_message(
        "MOTIVATION NINJA",
        f"🍥 **Message pour {user.first_name}** 🍥\n\n{motivation}\n\n🥷 *Continue ton chemin ninja!*",
        "💪"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def playaudio_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /playaudio"""
    query = ' '.join(context.args) if context.args else "naruto opening"
    
    message = format_naruto_message(
        "LECTURE AUDIO NINJA",
        f"🎵 Recherche audio: {query}\n🎧 Préparation de la playlist ninja...\n\n*Fonctionnalité en développement*",
        "🎵"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def playvideo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /playvideo"""
    query = ' '.join(context.args) if context.args else "naruto amv"
    
    message = format_naruto_message(
        "LECTURE VIDÉO NINJA",
        f"🎬 Recherche vidéo: {query}\n📺 Préparation du cinéma ninja...\n\n*Fonctionnalité en développement*",
        "🎬"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def youtube_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /youtube"""
    query = ' '.join(context.args) if context.args else "naruto"
    
    message = format_naruto_message(
        "RECHERCHE YOUTUBE NINJA",
        f"🔍 Recherche YouTube: {query}\n📺 Scan des vidéos avec le Sharingan...\n\n*Fonctionnalité en développement*",
        "📺"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def tiktok_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /tiktok"""
    query = ' '.join(context.args) if context.args else "naruto"
    
    message = format_naruto_message(
        "RECHERCHE TIKTOK NINJA",
        f"📱 Recherche TikTok: {query}\n🎭 Scan des vidéos courtes ninja...\n\n*Fonctionnalité en développement*",
        "📱"
    )
    await update.message.reply_text(message, parse_mode='Markdown')