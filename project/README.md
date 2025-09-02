# 🍥 TSUKIBOT - Bot Telegram Thème Naruto

## 📋 Description
TSUKIBOT est un bot Telegram complet avec un thème Naruto, créé par @jeff_mitsuki. Il offre des fonctionnalités de gestion de groupe, médias, stockage et divertissement avec un style ninja!

## 🚀 Installation

### Prérequis
- Python 3.8+
- pip (gestionnaire de paquets Python)

### Installation des dépendances
```bash
pip install -r requirements.txt
```

### Configuration
1. Modifiez le fichier `config.py` avec vos informations:
   - BOT_TOKEN: Token de votre bot Telegram
   - OWNER_ID: Votre ID utilisateur Telegram
   - OWNER_USERNAME: Votre nom d'utilisateur Telegram

2. Créez les dossiers nécessaires (automatique au premier lancement):
   - `data/` - Stockage des données utilisateurs
   - `logs/` - Fichiers de logs
   - `media/` - Médias stockés

## 🎮 Lancement
```bash
python bot.py
```

## 🥷 Fonctionnalités

### 📋 Commandes Générales
- `/start` - Menu principal avec ASCII art ninja
- `/ping` - Vérifier le statut du bot
- `/date` - Date et heure actuelles
- `/contact` - Contacter le développeur
- `/info` - Informations de l'utilisateur
- `/quote` - Citation Naruto aléatoire
- `/setpp` - Définir photo de profil
- `/getpp` - Récupérer photo de profil
- `/autoreact` - Mode auto-réaction
- `/autowrite` - Mode auto-écriture
- `/take` - Capturer un message

### 🎭 Commandes Médias
- `/img` - Rechercher des images
- `/gif` - Rechercher des GIFs
- `/vid` - Rechercher des vidéos
- `/aud` - Rechercher de l'audio
- `/stk` - Créer un sticker
- `/tostk` - Convertir image en sticker
- `/vu` - Créer une vue temporaire

### 💾 Commandes Stockage
- `/store` - Stocker un média
- `/list` - Lister les médias stockés
- `/delmedia` - Supprimer un média

### ⚔️ Commandes Administration
- `/welcome` - Configurer message de bienvenue
- `/antilink` - Protection anti-liens
- `/promote` - Promouvoir un membre
- `/promoteall` - Promouvoir tous les membres
- `/demote` - Rétrograder un membre
- `/demoteall` - Rétrograder tous les admins
- `/kick` - Expulser un membre
- `/kickall` - Expulser tous les membres
- `/mute` - Rendre muet un utilisateur
- `/unmute` - Enlever le mode muet
- `/tagadmin` - Taguer tous les admins
- `/tagall` - Taguer tous les membres
- `/groupinfo` - Informations du groupe
- `/antimedia` - Protection anti-médias
- `/antibot` - Protection anti-bots
- `/antispam` - Protection anti-spam
- `/antiedit` - Protection anti-édition
- `/antiforward` - Protection anti-transfert
- `/antivoice` - Protection anti-vocal
- `/listusers` - Lister utilisateurs (Owner uniquement)

### 🎮 Commandes Divertissement
- `/motivation` - Message motivant personnalisé
- `/playaudio` - Jouer de l'audio
- `/playvideo` - Jouer une vidéo
- `/youtube` - Rechercher sur YouTube
- `/tiktok` - Rechercher sur TikTok

### ❓ Commandes Aide
- `/help` - Aide détaillée
- `/doc` - Documentation complète
- `/updates` - Mises à jour du bot
- `/about` - À propos du bot

## 🎯 Fonctionnalités Spéciales

### 👥 Tracking des Utilisateurs
- Enregistrement automatique à chaque `/start`
- Sauvegarde ID, username, first_name dans `users.json`
- Commande `/listusers` pour le propriétaire

### 🍥 Thème Naruto
- Citations inspirantes de Naruto
- Emojis ninja dans tous les messages
- Messages stylisés et colorés
- ASCII art ninja

### 🛡️ Sécurité
- Commandes admin restreintes
- Vérification des permissions
- Protection contre les abus
- Logs des erreurs

## 📁 Structure du Projet
```
TSUKIBOT/
├── bot.py              # Fichier principal
├── config.py           # Configuration
├── requirements.txt    # Dépendances
├── handlers/           # Gestionnaires de commandes
│   ├── general.py      # Commandes générales
│   ├── media.py        # Commandes médias
│   ├── storage.py      # Commandes stockage
│   ├── admin.py        # Commandes administration
│   ├── entertainment.py # Commandes divertissement
│   └── help.py         # Commandes aide
├── utils/              # Utilitaires
│   ├── user_tracker.py # Tracking utilisateurs
│   └── helpers.py      # Fonctions utiles
├── data/               # Données stockées
├── logs/               # Fichiers de logs
└── media/              # Médias stockés
```

## 🔧 Configuration Avancée

### Variables d'environnement
Vous pouvez utiliser un fichier `.env` pour la configuration:
```env
BOT_TOKEN=votre_token_ici
OWNER_ID=votre_id_ici
OWNER_USERNAME=@votre_username
```

### Personnalisation
- Modifiez `NARUTO_QUOTES` dans `config.py` pour ajouter des citations
- Ajustez `NINJA_EMOJIS` pour changer les emojis utilisés
- Personnalisez `WELCOME_BANNER` pour l'ASCII art

## 🤝 Contribution
Les contributions sont les bienvenues! N'hésitez pas à proposer des améliorations.

## 📄 Licence
Projet personnel - Utilisation libre

## 🍥 Crédits
Créé avec ❤️ par @jeff_mitsuki
Inspiré par l'univers Naruto de Masashi Kishimoto

---
*"Crois en ton potentiel ninja!" - Naruto Uzumaki* 🥷