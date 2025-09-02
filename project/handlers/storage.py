"""
Handlers pour les commandes de stockage
"""

from telegram import Update
from telegram.ext import ContextTypes
import json
import os
from datetime import datetime
from utils.helpers import format_naruto_message

STORAGE_FILE = "data/media_storage.json"

async def store_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /store"""
    if not update.message.reply_to_message:
        message = format_naruto_message(
            "STOCKAGE NINJA",
            "❌ Répondez à un média (photo, vidéo, audio, document) pour le stocker!",
            "💾"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    # Simuler le stockage
    user = update.effective_user
    media_type = "unknown"
    file_id = "simulation"
    
    if update.message.reply_to_message.photo:
        media_type = "photo"
        file_id = update.message.reply_to_message.photo[-1].file_id
    elif update.message.reply_to_message.video:
        media_type = "video"
        file_id = update.message.reply_to_message.video.file_id
    elif update.message.reply_to_message.audio:
        media_type = "audio"
        file_id = update.message.reply_to_message.audio.file_id
    
    # Charger ou créer le fichier de stockage
    try:
        if os.path.exists(STORAGE_FILE):
            with open(STORAGE_FILE, 'r', encoding='utf-8') as f:
                storage_data = json.load(f)
        else:
            storage_data = {"media": []}
        
        # Ajouter le nouveau média
        media_entry = {
            "id": len(storage_data["media"]) + 1,
            "file_id": file_id,
            "type": media_type,
            "stored_by": user.id,
            "stored_by_name": user.first_name,
            "stored_date": datetime.now().isoformat(),
            "name": ' '.join(context.args) if context.args else f"Média {len(storage_data['media']) + 1}"
        }
        
        storage_data["media"].append(media_entry)
        
        # Sauvegarder
        with open(STORAGE_FILE, 'w', encoding='utf-8') as f:
            json.dump(storage_data, f, indent=2, ensure_ascii=False)
        
        message = format_naruto_message(
            "STOCKAGE RÉUSSI",
            f"✅ Média stocké avec succès!\n📁 Type: {media_type}\n🏷️ Nom: {media_entry['name']}\n🆔 ID: {media_entry['id']}",
            "💾"
        )
        
    except Exception as e:
        message = format_naruto_message(
            "ERREUR STOCKAGE",
            f"❌ Erreur lors du stockage: {str(e)}",
            "❌"
        )
    
    await update.message.reply_text(message, parse_mode='Markdown')

async def list_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /list"""
    try:
        if not os.path.exists(STORAGE_FILE):
            message = format_naruto_message(
                "LISTE DES MÉDIAS",
                "📁 Aucun média stocké pour le moment!",
                "📁"
            )
            await update.message.reply_text(message, parse_mode='Markdown')
            return
        
        with open(STORAGE_FILE, 'r', encoding='utf-8') as f:
            storage_data = json.load(f)
        
        if not storage_data["media"]:
            message = format_naruto_message(
                "LISTE DES MÉDIAS",
                "📁 Aucun média stocké pour le moment!",
                "📁"
            )
        else:
            media_list = "📁 **MÉDIAS STOCKÉS** 📁\n\n"
            for media in storage_data["media"]:
                media_list += f"{media['id']}. **{media['name']}**\n"
                media_list += f"   📷 Type: {media['type']}\n"
                media_list += f"   👤 Par: {media['stored_by_name']}\n"
                media_list += f"   📅 Date: {media['stored_date'][:10]}\n\n"
            
            media_list += f"\n🍥 {get_random_naruto_quote()}"
            message = media_list
        
    except Exception as e:
        message = format_naruto_message(
            "ERREUR LISTE",
            f"❌ Erreur lors de la récupération: {str(e)}",
            "❌"
        )
    
    await update.message.reply_text(message, parse_mode='Markdown')

async def delmedia_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /delmedia"""
    if not context.args:
        message = format_naruto_message(
            "SUPPRESSION MÉDIA",
            "❌ Spécifiez l'ID du média à supprimer!\nExemple: `/delmedia 1`",
            "🗑️"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    try:
        media_id = int(context.args[0])
        
        if os.path.exists(STORAGE_FILE):
            with open(STORAGE_FILE, 'r', encoding='utf-8') as f:
                storage_data = json.load(f)
            
            # Chercher et supprimer le média
            media_found = False
            for i, media in enumerate(storage_data["media"]):
                if media["id"] == media_id:
                    storage_data["media"].pop(i)
                    media_found = True
                    break
            
            if media_found:
                # Sauvegarder les changements
                with open(STORAGE_FILE, 'w', encoding='utf-8') as f:
                    json.dump(storage_data, f, indent=2, ensure_ascii=False)
                
                message = format_naruto_message(
                    "SUPPRESSION RÉUSSIE",
                    f"✅ Média ID {media_id} supprimé avec succès!",
                    "🗑️"
                )
            else:
                message = format_naruto_message(
                    "MÉDIA INTROUVABLE",
                    f"❌ Aucun média avec l'ID {media_id} trouvé!",
                    "🗑️"
                )
        else:
            message = format_naruto_message(
                "AUCUN STOCKAGE",
                "❌ Aucun fichier de stockage trouvé!",
                "🗑️"
            )
    
    except ValueError:
        message = format_naruto_message(
            "ID INVALIDE",
            "❌ L'ID doit être un nombre valide!",
            "🗑️"
        )
    except Exception as e:
        message = format_naruto_message(
            "ERREUR SUPPRESSION",
            f"❌ Erreur: {str(e)}",
            "❌"
        )
    
    await update.message.reply_text(message, parse_mode='Markdown')