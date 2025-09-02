"""
TSUKIBOT - Bot Telegram avec thème Naruto
Créé par @jeff_mitsuki
"""

import logging
import json
import os
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio
import random

from config import *
from handlers.general import *
from handlers.media import *
from handlers.storage import *
from handlers.admin import *
from handlers.entertainment import *
from handlers.help import *
from utils.user_tracker import track_user, is_owner
from utils.helpers import get_random_naruto_quote, get_ninja_emoji

# Configuration du logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Initialisation des dossiers
os.makedirs("data", exist_ok=True)
os.makedirs("media", exist_ok=True)
os.makedirs("logs", exist_ok=True)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /start avec menu principal"""
    user = update.effective_user
    chat = update.effective_chat
    
    # Tracker l'utilisateur
    await track_user(user)
    
    # Photo de bienvenue Naruto (URL Pexels)
    naruto_photo = "https://images.pexels.com/photos/8923533/pexels-photo-8923533.jpeg"
    
    # Message de bienvenue personnalisé
    welcome_text = f"""
{WELCOME_BANNER}

🍥 **Salut {user.first_name}!** 🍥

Bienvenue dans l'univers ninja de TSUKIBOT! 
Je suis ton assistant personnel inspiré de Naruto Uzumaki!

{get_random_naruto_quote()}

{MAIN_MENU}

🥷 *Prêt pour l'aventure ninja?* {get_ninja_emoji()}
"""
    
    # Envoyer la photo avec le message
    await context.bot.send_photo(
        chat_id=chat.id,
        photo=naruto_photo,
        caption=welcome_text,
        parse_mode='Markdown'
    )

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handler d'erreurs global"""
    logger.error(f"Exception while handling an update: {context.error}")
    
    if isinstance(update, Update) and update.effective_chat:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"🚫 Une erreur s'est produite! {get_ninja_emoji()}\n\n*L'erreur sera signalée au développeur.*",
            parse_mode='Markdown'
        )

def main():
    """Fonction principale du bot"""
    # Créer l'application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Handlers principaux
    application.add_handler(CommandHandler("start", start_command))
    
    # Handlers généraux
    application.add_handler(CommandHandler("ping", ping_command))
    application.add_handler(CommandHandler("date", date_command))
    application.add_handler(CommandHandler("contact", contact_command))
    application.add_handler(CommandHandler("info", info_command))
    application.add_handler(CommandHandler("quote", quote_command))
    application.add_handler(CommandHandler("setpp", setpp_command))
    application.add_handler(CommandHandler("getpp", getpp_command))
    application.add_handler(CommandHandler("autoreact", autoreact_command))
    application.add_handler(CommandHandler("autowrite", autowrite_command))
    application.add_handler(CommandHandler("take", take_command))
    
    # Handlers médias
    application.add_handler(CommandHandler("img", img_command))
    application.add_handler(CommandHandler("gif", gif_command))
    application.add_handler(CommandHandler("vid", vid_command))
    application.add_handler(CommandHandler("aud", aud_command))
    application.add_handler(CommandHandler("stk", stk_command))
    application.add_handler(CommandHandler("tostk", tostk_command))
    application.add_handler(CommandHandler("vu", vu_command))
    
    # Handlers stockage
    application.add_handler(CommandHandler("store", store_command))
    application.add_handler(CommandHandler("list", list_command))
    application.add_handler(CommandHandler("delmedia", delmedia_command))
    
    # Handlers administration
    application.add_handler(CommandHandler("welcome", welcome_command))
    application.add_handler(CommandHandler("antilink", antilink_command))
    application.add_handler(CommandHandler("promote", promote_command))
    application.add_handler(CommandHandler("promoteall", promoteall_command))
    application.add_handler(CommandHandler("demote", demote_command))
    application.add_handler(CommandHandler("demoteall", demoteall_command))
    application.add_handler(CommandHandler("kick", kick_command))
    application.add_handler(CommandHandler("kickall", kickall_command))
    application.add_handler(CommandHandler("mute", mute_command))
    application.add_handler(CommandHandler("unmute", unmute_command))
    application.add_handler(CommandHandler("tagadmin", tagadmin_command))
    application.add_handler(CommandHandler("tagall", tagall_command))
    application.add_handler(CommandHandler("groupinfo", groupinfo_command))
    application.add_handler(CommandHandler("antimedia", antimedia_command))
    application.add_handler(CommandHandler("antibot", antibot_command))
    application.add_handler(CommandHandler("antispam", antispam_command))
    application.add_handler(CommandHandler("antiedit", antiedit_command))
    application.add_handler(CommandHandler("antiforward", antiforward_command))
    application.add_handler(CommandHandler("antivoice", antivoice_command))
    application.add_handler(CommandHandler("listusers", listusers_command))
    
    # Handlers divertissement
    application.add_handler(CommandHandler("motivation", motivation_command))
    application.add_handler(CommandHandler("playaudio", playaudio_command))
    application.add_handler(CommandHandler("playvideo", playvideo_command))
    application.add_handler(CommandHandler("youtube", youtube_command))
    application.add_handler(CommandHandler("tiktok", tiktok_command))
    
    # Handlers aide
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("doc", doc_command))
    application.add_handler(CommandHandler("updates", updates_command))
    application.add_handler(CommandHandler("about", about_command))
    
    # Handler d'erreurs
    application.add_error_handler(error_handler)
    
    # Démarrer le bot
    print(f"🍥 {BOT_NAME} démarré avec succès! 🥷")
    print(f"📱 Owner: {OWNER_USERNAME}")
    print(f"🚀 Bot prêt à recevoir des commandes...")
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()