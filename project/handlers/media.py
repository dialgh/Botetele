"""
Handlers pour les commandes médias
"""

from telegram import Update
from telegram.ext import ContextTypes
from utils.helpers import format_naruto_message, get_ninja_emoji

async def img_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /img"""
    query = ' '.join(context.args) if context.args else "naruto"
    
    # URLs d'images Naruto depuis Pexels
    naruto_images = [
        "https://images.pexels.com/photos/8923533/pexels-photo-8923533.jpeg",
        "https://images.pexels.com/photos/6003442/pexels-photo-6003442.jpeg",
        "https://images.pexels.com/photos/7095306/pexels-photo-7095306.jpeg"
    ]
    
    import random
    selected_image = random.choice(naruto_images)
    
    caption = format_naruto_message(
        "RECHERCHE D'IMAGE NINJA",
        f"🖼️ Recherche: {query}\n🎯 Image trouvée avec la technique ninja!",
        "🖼️"
    )
    
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=selected_image,
        caption=caption,
        parse_mode='Markdown'
    )

async def gif_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /gif"""
    query = ' '.join(context.args) if context.args else "naruto"
    
    message = format_naruto_message(
        "RECHERCHE GIF NINJA",
        f"🎞️ Recherche de GIF: {query}\n⚡ Technique de recherche en cours...\n\n*Fonctionnalité en développement*",
        "🎞️"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def vid_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /vid"""
    query = ' '.join(context.args) if context.args else "naruto"
    
    message = format_naruto_message(
        "RECHERCHE VIDÉO NINJA",
        f"🎬 Recherche de vidéo: {query}\n🔍 Scan en cours avec le Byakugan...\n\n*Fonctionnalité en développement*",
        "🎬"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def aud_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /aud"""
    query = ' '.join(context.args) if context.args else "naruto"
    
    message = format_naruto_message(
        "RECHERCHE AUDIO NINJA",
        f"🎵 Recherche audio: {query}\n🎧 Écoute attentive en cours...\n\n*Fonctionnalité en développement*",
        "🎵"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def stk_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /stk"""
    message = format_naruto_message(
        "CRÉATION STICKER NINJA",
        "🎨 Pour créer un sticker personnalisé:\n1. Envoyez une image\n2. Je la transformerai en sticker ninja!\n\n*Fonctionnalité en développement*",
        "🎨"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def tostk_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /tostk"""
    if update.message.reply_to_message and update.message.reply_to_message.photo:
        message = format_naruto_message(
            "CONVERSION EN STICKER",
            "🎨 Image détectée! Conversion en sticker ninja en cours...\n\n*Fonctionnalité en développement*",
            "🎨"
        )
    else:
        message = format_naruto_message(
            "CONVERSION EN STICKER",
            "❌ Répondez à une image pour la convertir en sticker!",
            "🎨"
        )
    
    await update.message.reply_text(message, parse_mode='Markdown')

async def vu_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /vu (vue temporaire)"""
    message = format_naruto_message(
        "VUE TEMPORAIRE NINJA",
        "👁️ Création d'une vue temporaire avec technique de disparition!\n⏱️ Le contenu s'auto-détruira...\n\n*Fonctionnalité en développement*",
        "👁️"
    )
    await update.message.reply_text(message, parse_mode='Markdown')