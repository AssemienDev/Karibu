from django.contrib import admin

# Register your models here.

from utilisateur.models import Utilisateur,Chambre,ChambreClimatisee

@admin.register(Utilisateur)

#classe pour lister les utilisateurs du site

class list_user (admin.ModelAdmin):
    list_display = (
        "nom_complet",
        "mail_utilisateur",
        
    )


@admin.register(Chambre)
#classe pour lister la liste des chambres

class list_chambre (admin.ModelAdmin):
    list_display = (
        "statutChambre",
        "chambre_climatisee",
        "chambre_ventilee",
        "suite",
    )

    search_field = (
        "statutChambre",
        "chambre_climatisee",
        "chambre_ventilee",
        "suite",
    )


@admin.register(ChambreClimatisee)
#classe pour lister la liste des chambres climatisées

class list_ChambreClimatisee (admin.ModelAdmin):
    list_display = (
        "numeroChambre",
        "description",
        "prix_nuite",
        "prix_journee",
    )

    search_field = (
       "numeroChambre",
        "description",
        "prix_nuite",
        "prix_journee",
    )

