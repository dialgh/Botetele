"""
Système de tracking des utilisateurs TSUKIBOT
"""

import json
import os
from datetime import datetime
from telegram import User
from config import USERS_FILE, OWNER_ID

async def track_user(user: User):
    """Enregistre un utilisateur dans le fichier JSON"""
    try:
        # Charger les utilisateurs existants
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, 'r', encoding='utf-8') as f:
                users_data = json.load(f)
        else:
            users_data = {"users": [], "total_users": 0, "last_updated": ""}
        
        # Vérifier si l'utilisateur existe déjà
        user_exists = any(u['id'] == user.id for u in users_data['users'])
        
        if not user_exists:
            # Ajouter le nouvel utilisateur
            new_user = {
                "id": user.id,
                "username": user.username or "Aucun",
                "first_name": user.first_name or "Inconnu",
                "last_name": user.last_name or "",
                "language_code": user.language_code or "Unknown",
                "first_seen": datetime.now().isoformat(),
                "last_interaction": datetime.now().isoformat()
            }
            
            users_data['users'].append(new_user)
            users_data['total_users'] = len(users_data['users'])
            users_data['last_updated'] = datetime.now().isoformat()
            
            # Sauvegarder
            with open(USERS_FILE, 'w', encoding='utf-8') as f:
                json.dump(users_data, f, indent=2, ensure_ascii=False)
        else:
            # Mettre à jour la dernière interaction
            for user_data in users_data['users']:
                if user_data['id'] == user.id:
                    user_data['last_interaction'] = datetime.now().isoformat()
                    break
            
            # Sauvegarder les changements
            with open(USERS_FILE, 'w', encoding='utf-8') as f:
                json.dump(users_data, f, indent=2, ensure_ascii=False)
                
    except Exception as e:
        print(f"Erreur lors du tracking utilisateur: {e}")

def is_owner(user_id: int) -> bool:
    """Vérifie si l'utilisateur est le propriétaire du bot"""
    return user_id == OWNER_ID

async def get_all_users():
    """Récupère tous les utilisateurs trackés"""
    try:
        if os.path.exists(USERS_FILE):
            with open(USERS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"users": [], "total_users": 0}
    except Exception as e:
        print(f"Erreur lors de la récupération des utilisateurs: {e}")
        return {"users": [], "total_users": 0}