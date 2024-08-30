from django.contrib import admin

# Register your models here.

from utilisateur.models import Utilisateur

@admin.register(Utilisateur)

#classe pour lister les utilisateurs du site

class list_user (admin.ModelAdmin):
    list_display = (
        "nom_complet",
        "mail_utilisateur",
        
    )