"""
Handlers pour les commandes d'administration
"""

from telegram import Update, ChatMember
from telegram.ext import ContextTypes
from utils.helpers import format_naruto_message, get_ninja_emoji
from utils.user_tracker import is_owner, get_all_users
from config import OWNER_ID

async def check_admin_rights(update: Update, context: ContextTypes.DEFAULT_TYPE) -> bool:
    """Vérifie les droits d'administration"""
    user = update.effective_user
    chat = update.effective_chat
    
    if chat.type == 'private':
        return True
    
    try:
        member = await context.bot.get_chat_member(chat.id, user.id)
        return member.status in ['administrator', 'creator'] or user.id == OWNER_ID
    except:
        return False

async def welcome_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /welcome"""
    if not await check_admin_rights(update, context):
        message = format_naruto_message(
            "ACCÈS REFUSÉ",
            "❌ Seuls les administrateurs peuvent configurer le message de bienvenue!",
            "🚫"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    message = format_naruto_message(
        "MESSAGE DE BIENVENUE",
        "🎉 Configuration du message de bienvenue ninja!\n✨ Les nouveaux membres recevront un accueil digne du Village de la Feuille!",
        "🎉"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def antilink_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /antilink"""
    if not await check_admin_rights(update, context):
        message = format_naruto_message(
            "ACCÈS REFUSÉ",
            "❌ Seuls les administrateurs peuvent activer la protection anti-liens!",
            "🚫"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    message = format_naruto_message(
        "PROTECTION ANTI-LIENS",
        "🛡️ Protection anti-liens activée!\n⚔️ Technique de défense ninja contre les liens malveillants!",
        "🛡️"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def promote_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /promote"""
    if not await check_admin_rights(update, context):
        message = format_naruto_message(
            "ACCÈS REFUSÉ",
            "❌ Seuls les administrateurs peuvent promouvoir des membres!",
            "🚫"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    if update.message.reply_to_message:
        user = update.message.reply_to_message.from_user
        message = format_naruto_message(
            "PROMOTION NINJA",
            f"⬆️ {user.first_name} a été promu(e) au rang de ninja!\n🎖️ Nouveaux pouvoirs administratifs accordés!",
            "⬆️"
        )
    else:
        message = format_naruto_message(
            "PROMOTION NINJA",
            "❌ Répondez au message d'un utilisateur pour le promouvoir!",
            "⬆️"
        )
    
    await update.message.reply_text(message, parse_mode='Markdown')

async def promoteall_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /promoteall"""
    if not is_owner(update.effective_user.id):
        message = format_naruto_message(
            "ACCÈS REFUSÉ",
            "❌ Seul le propriétaire du bot peut promouvoir tous les membres!",
            "🚫"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    message = format_naruto_message(
        "PROMOTION MASSIVE",
        "⬆️ Promotion de tous les membres en cours!\n🎖️ Transformation en armée ninja!",
        "⬆️"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def demote_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /demote"""
    if not await check_admin_rights(update, context):
        message = format_naruto_message(
            "ACCÈS REFUSÉ",
            "❌ Seuls les administrateurs peuvent rétrograder des membres!",
            "🚫"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    if update.message.reply_to_message:
        user = update.message.reply_to_message.from_user
        message = format_naruto_message(
            "RÉTROGRADATION NINJA",
            f"⬇️ {user.first_name} a été rétrogradé(e)!\n📉 Pouvoirs administratifs retirés!",
            "⬇️"
        )
    else:
        message = format_naruto_message(
            "RÉTROGRADATION NINJA",
            "❌ Répondez au message d'un utilisateur pour le rétrograder!",
            "⬇️"
        )
    
    await update.message.reply_text(message, parse_mode='Markdown')

async def demoteall_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /demoteall"""
    if not is_owner(update.effective_user.id):
        message = format_naruto_message(
            "ACCÈS REFUSÉ",
            "❌ Seul le propriétaire du bot peut rétrograder tous les membres!",
            "🚫"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    message = format_naruto_message(
        "RÉTROGRADATION MASSIVE",
        "⬇️ Rétrogradation de tous les admins en cours!\n📉 Retour au statut de genin!",
        "⬇️"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def kick_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /kick"""
    if not await check_admin_rights(update, context):
        message = format_naruto_message(
            "ACCÈS REFUSÉ",
            "❌ Seuls les administrateurs peuvent expulser des membres!",
            "🚫"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    if update.message.reply_to_message:
        user = update.message.reply_to_message.from_user
        message = format_naruto_message(
            "EXPULSION NINJA",
            f"👢 {user.first_name} a été expulsé(e) du groupe!\n⚡ Technique de bannissement activée!",
            "👢"
        )
    else:
        message = format_naruto_message(
            "EXPULSION NINJA",
            "❌ Répondez au message d'un utilisateur pour l'expulser!",
            "👢"
        )
    
    await update.message.reply_text(message, parse_mode='Markdown')

async def kickall_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /kickall"""
    if not is_owner(update.effective_user.id):
        message = format_naruto_message(
            "ACCÈS REFUSÉ",
            "❌ Seul le propriétaire du bot peut expulser tous les membres!",
            "🚫"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    message = format_naruto_message(
        "EXPULSION MASSIVE",
        "👢 Expulsion de tous les membres en cours!\n💥 Technique interdite activée!",
        "👢"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def mute_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /mute"""
    if not await check_admin_rights(update, context):
        message = format_naruto_message(
            "ACCÈS REFUSÉ",
            "❌ Seuls les administrateurs peuvent rendre muets les membres!",
            "🚫"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    if update.message.reply_to_message:
        user = update.message.reply_to_message.from_user
        message = format_naruto_message(
            "TECHNIQUE DU SILENCE",
            f"🤐 {user.first_name} a été rendu(e) muet(te)!\n🥷 Technique ninja du silence appliquée!",
            "🤐"
        )
    else:
        message = format_naruto_message(
            "TECHNIQUE DU SILENCE",
            "❌ Répondez au message d'un utilisateur pour le rendre muet!",
            "🤐"
        )
    
    await update.message.reply_text(message, parse_mode='Markdown')

async def unmute_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /unmute"""
    if not await check_admin_rights(update, context):
        message = format_naruto_message(
            "ACCÈS REFUSÉ",
            "❌ Seuls les administrateurs peuvent enlever le mode muet!",
            "🚫"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    if update.message.reply_to_message:
        user = update.message.reply_to_message.from_user
        message = format_naruto_message(
            "LIBÉRATION DE LA PAROLE",
            f"🔊 {user.first_name} peut de nouveau parler!\n🗣️ Technique ninja de libération appliquée!",
            "🔊"
        )
    else:
        message = format_naruto_message(
            "LIBÉRATION DE LA PAROLE",
            "❌ Répondez au message d'un utilisateur pour enlever le mode muet!",
            "🔊"
        )
    
    await update.message.reply_text(message, parse_mode='Markdown')

async def tagadmin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /tagadmin"""
    message = format_naruto_message(
        "APPEL DES ADMINISTRATEURS",
        "📢 @admin @admin @admin\n🚨 Tous les administrateurs ninja sont appelés!",
        "📢"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def tagall_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /tagall"""
    if not await check_admin_rights(update, context):
        message = format_naruto_message(
            "ACCÈS REFUSÉ",
            "❌ Seuls les administrateurs peuvent taguer tous les membres!",
            "🚫"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    message = format_naruto_message(
        "APPEL GÉNÉRAL NINJA",
        "📢 Tous les ninjas du groupe sont appelés!\n🥷 Rassemblement général en cours!",
        "📢"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def groupinfo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /groupinfo"""
    chat = update.effective_chat
    
    if chat.type == 'private':
        message = format_naruto_message(
            "INFORMATION CHAT",
            "📱 Chat privé avec TSUKIBOT\n🥷 Mode conversation ninja activé!",
            "ℹ️"
        )
    else:
        info = f"""
📋 **Nom**: {chat.title or 'Groupe sans nom'}
🆔 **ID**: `{chat.id}`
👥 **Type**: {chat.type}
📝 **Description**: {chat.description or 'Aucune description'}
"""
        message = format_naruto_message("INFORMATIONS DU GROUPE", info, "ℹ️")
    
    await update.message.reply_text(message, parse_mode='Markdown')

async def antimedia_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /antimedia"""
    if not await check_admin_rights(update, context):
        message = format_naruto_message(
            "ACCÈS REFUSÉ",
            "❌ Seuls les administrateurs peuvent activer la protection anti-médias!",
            "🚫"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    message = format_naruto_message(
        "PROTECTION ANTI-MÉDIAS",
        "🛡️ Protection anti-médias activée!\n📵 Technique ninja de blocage des médias indésirables!",
        "🛡️"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def antibot_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /antibot"""
    if not await check_admin_rights(update, context):
        message = format_naruto_message(
            "ACCÈS REFUSÉ",
            "❌ Seuls les administrateurs peuvent activer la protection anti-bots!",
            "🚫"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    message = format_naruto_message(
        "PROTECTION ANTI-BOTS",
        "🤖 Protection anti-bots activée!\n🛡️ Technique ninja contre les bots malveillants!",
        "🤖"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def antispam_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /antispam"""
    if not await check_admin_rights(update, context):
        message = format_naruto_message(
            "ACCÈS REFUSÉ",
            "❌ Seuls les administrateurs peuvent activer la protection anti-spam!",
            "🚫"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    message = format_naruto_message(
        "PROTECTION ANTI-SPAM",
        "🚫 Protection anti-spam activée!\n⚡ Technique ninja de filtrage des messages répétitifs!",
        "🚫"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def antiedit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /antiedit"""
    if not await check_admin_rights(update, context):
        message = format_naruto_message(
            "ACCÈS REFUSÉ",
            "❌ Seuls les administrateurs peuvent activer la protection anti-édition!",
            "🚫"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    message = format_naruto_message(
        "PROTECTION ANTI-ÉDITION",
        "✏️ Protection anti-édition activée!\n🔒 Technique ninja de verrouillage des messages!",
        "✏️"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def antiforward_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /antiforward"""
    if not await check_admin_rights(update, context):
        message = format_naruto_message(
            "ACCÈS REFUSÉ",
            "❌ Seuls les administrateurs peuvent activer la protection anti-transfert!",
            "🚫"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    message = format_naruto_message(
        "PROTECTION ANTI-TRANSFERT",
        "📤 Protection anti-transfert activée!\n🛡️ Technique ninja contre les messages transférés!",
        "📤"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def antivoice_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /antivoice"""
    if not await check_admin_rights(update, context):
        message = format_naruto_message(
            "ACCÈS REFUSÉ",
            "❌ Seuls les administrateurs peuvent activer la protection anti-vocal!",
            "🚫"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    message = format_naruto_message(
        "PROTECTION ANTI-VOCAL",
        "🔇 Protection anti-vocal activée!\n🤫 Technique ninja du silence vocal!",
        "🔇"
    )
    await update.message.reply_text(message, parse_mode='Markdown')

async def listusers_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Commande /listusers (Réservée au propriétaire)"""
    if not is_owner(update.effective_user.id):
        message = format_naruto_message(
            "ACCÈS REFUSÉ",
            "❌ Cette commande est réservée au propriétaire du bot!",
            "🚫"
        )
        await update.message.reply_text(message, parse_mode='Markdown')
        return
    
    try:
        users_data = await get_all_users()
        if users_data['total_users'] == 0:
            message = format_naruto_message(
                "LISTE DES UTILISATEURS",
                "👥 Aucun utilisateur enregistré pour le moment!",
                "👥"
            )
        else:
            from utils.helpers import format_user_list
            message = format_user_list(users_data)
    
    except Exception as e:
        message = format_naruto_message(
            "ERREUR",
            f"❌ Erreur lors de la récupération: {str(e)}",
            "❌"
        )
    
    await update.message.reply_text(message, parse_mode='Markdown')