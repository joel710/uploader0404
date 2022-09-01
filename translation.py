class Translation(object):

    START_TEXT = """<b>Bonjour, 
    Il s'agit d'un bot de téléchargement d'URL Telegram ! 
    Veuillez m'envoyer tout lien URL de téléchargement direct, je peux télécharger sur télégramme en tant que fichier/vidéo </b>
/help pour plus de détails..Canal d'assistance : https://t.me/AD_tecknobot
"""

    HELP_USER = """Hi  je suis jojo_url_uploader_bot ..
    
1. Envoyer l'URL (Lien | Nouveau nom avec extension).
2. Envoyer une vignette personnalisée (facultatif).
3. Sélectionnez le bouton.
   SVideo - Donner le fichier en vidéo avec des captures d'écran
   DFile  - Donner un fichier avec des captures d'écran
   Video  - Donner le fichier sous forme de vidéo sans captures d'écran
   DFile  - Donner un fichier sans captures d'écran
Canal d'assistance : https://t.me/AD_tecknobot
"""

    FORMAT_SELECTION = """Sélectionnez le format souhaité: <a href='{}'>file size might be approximate</a>
    
Envoyez votre vignette personnalisée si nécessaire.
Vous pouvez utiliser /deletethumbnail pour supprimer la vignette générée automatiquement."""
    
    SET_CUSTOM_USERNAME_PASSWORD = """Si vous souhaitez télécharger des vidéos premium, fournissez-les au format suivant :
URL | newfilename | username | password"""


    UPGRADE_TEXT = "<b>👉 Create Bot.. </b>  \n\n<a href='http'>Click here, Fork and deploy!!</a>"
    
    DOWNLOAD_START = "Essayer de télécharger votre fichier..."
    
    UPLOAD_START = "Télécharger maintenant.."
    
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Téléchargé en {} seconds. \n\nUploaded in {} seconds."

    RCHD_TG_API_LIMIT = "Téléchargé en {} seconds.\nDetected File Size: {}\nSorry. Mais je ne peux pas télécharger de fichiers supérieurs à 1,95 Go en raison des limitations de l'API Telegram."

    SAVED_CUSTOM_THUMB_NAIL = "Vignette personnalisée enregistrée. Ce sera définitif.\n\nUtilisation /deletethumbnail pour l'effacer."

    DEL_ETED_CUSTOM_THUMB_NAIL = "Vignette personnalisée effacée avec succès."

    CUSTOM_CAPTION_UL_FILE = " "

    SLOW_URL_DECED = "Gosh qui semble être une URL très lente. Puisque vous étiez en train de foutre en l'air ma maison, je ne suis pas d'humeur à télécharger ce fichier. En attendant, pourquoi n'essayez-vous pas ceci:==> https://shrtz.me/PtsVnf6 et obtenez-moi une URL rapide pour que je puisse télécharger sur Telegram, sans que je ralentisse pour les autres utilisateurs."

    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>YouTubeDL</b> said: {}"
    
    SHOW_THUMB = "Utilisation /deletethumbnail pour effacer cette vignette."
    
    NO_THUMB = "Aucune vignette enregistrée n'a été trouvée !!\n\nEnvoyez une image pour l'enregistrer en tant que vignette de façon permanente."    
