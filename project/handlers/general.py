"""
Handlers pour les commandes générales
"""

from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime
import random
from utils.helpers import format_naruto_message, get_ninja_emoji, get_random_naruto_quote
from config import OWNER_USERNAME

async def ping_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /ping"""
    response_time = "< 100ms"
    message = format_naruto_message(
        "PING NINJA", 
        f"🏃‍♂️ Bot actif et rapide comme Naruto!\n⚡ Temps de réponse: {response_time}",
        "⚡"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def date_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /date"""
    now = datetime.now()
    date_str = now.strftime("%d/%m/%Y")
    time_str = now.strftime("%H:%M:%S")
    
    message = format_naruto_message(
        "DATE & HEURE NINJA",
        f"📅 Date: {date_str}\n🕐 Heure: {time_str}\n🌍 Fuseau: UTC+0",
        "📅"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def contact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /contact"""
    message = format_naruto_message(
        "CONTACT DÉVELOPPEUR",
        f"👨‍💻 Développeur: {OWNER_USERNAME}\n📞 Contact: Telegram uniquement\n🛠️ Support: Questions techniques",
        "📞"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /info"""
    user = update.effective_user
    chat = update.effective_chat
    
    user_info = f"""
👤 **Nom**: {user.first_name} {user.last_name or ''}
🆔 **ID**: `{user.id}`
👥 **Username**: @{user.username or 'Non défini'}
🌍 **Langue**: {user.language_code or 'Inconnue'}
💬 **Type de chat**: {chat.type}
"""
    
    message = format_naruto_message("INFORMATIONS UTILISATEUR", user_info, "👤")
    await update.message.reply_text(message, parse_mode='Markdown')

async def quote_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /quote"""
    quote = get_random_naruto_quote()
    ninja_emoji = get_ninja_emoji()
    
    message = f"""
🍥 **CITATION NINJA DU JOUR** 🍥

{quote}

{ninja_emoji} *Sagesse du Village Caché de la Feuille* {ninja_emoji}
"""
    await update.message.reply_text(message, parse_mode='Markdown')

async def setpp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /setpp"""
    message = format_naruto_message(
        "DÉFINIR PHOTO DE PROFIL",
        "📸 Envoyez-moi une photo en réponse à cette commande pour définir votre photo de profil du groupe!",
        "📸"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def getpp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /getpp"""
    user = update.effective_user
    try:
        photos = await context.bot.get_user_profile_photos(user.id, limit=1)
        if photos.total_count > 0:
            photo = photos.photos[0][-1]  # Prendre la plus grande taille
            await context.bot.send_photo(
                chat_id=update.effective_chat.id,
                photo=photo.file_id,
                caption=f"📸 Photo de profil de {user.first_name} {get_ninja_emoji()}"
            )
        else:
            message = format_naruto_message(
                "PHOTO DE PROFIL",
                f"❌ {user.first_name} n'a pas de photo de profil!",
                "📸"
            )
            await update.message.reply_text(message, parse_mode='Markdown')
    except Exception as e:
        await update.message.reply_text(f"❌ Impossible de récupérer la photo: {str(e)}")

async def autoreact_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /autoreact"""
    message = format_naruto_message(
        "AUTO-RÉACTION NINJA",
        "🎭 Mode auto-réaction activé!\nLe bot réagira automatiquement aux messages avec des emojis ninja!",
        "🎭"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def autowrite_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /autowrite"""
    message = format_naruto_message(
        "AUTO-ÉCRITURE NINJA",
        "✍️ Mode auto-écriture activé!\nLe bot écrira automatiquement des messages motivants de temps en temps!",
        "✍️"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def take_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /take"""
    if update.message.reply_to_message:
        replied_message = update.message.reply_to_message
        message = format_naruto_message(
            "MESSAGE CAPTURÉ",
            f"📤 Message de {replied_message.from_user.first_name} capturé par la technique ninja!",
            "📤"
        )
    else:
        message = format_naruto_message(
            "CAPTURE NINJA",
            "❌ Répondez à un message pour utiliser la technique de capture!",
            "📤"
        )
    
    await update.message.reply_text(message, parse_mode='Markdown')