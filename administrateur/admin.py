from django.contrib import admin

# Register your models here.

from utilisateur.models import Utilisateur,Chambre,ChambreClimatisee,CommandeEspace,CommandeLogement

@admin.register(Utilisateur)

#classe pour lister les utilisateurs du site

class list_user (admin.ModelAdmin):
    list_display = (
        "nom_complet",
        "mail_utilisateur",
        "mot_de_passe"
        
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


@admin.register(CommandeEspace)
#classe pour lister la liste commandes espaces

class list_cmde_espace (admin.ModelAdmin):
    list_display = (
        "numero_contacter",
        "date_arriver",
        "espace_description",
        "client_nom_complet",
        "etat_commande",
    )

    search_field = (
        "numero_contacter",
        "date_arriver",
        "espace_description",
        "client_nom_complet",
        "etat_commande",
    )

@admin.register(CommandeLogement)
#classe pour lister la liste commmande logement 

class list_cmde_logement (admin.ModelAdmin):
    list_display = (
        "numero_contacter",
        "date_arriver",
        "heure_arriver",
        "temps_sejour",
        "chambre",
        "choixSejour",
        "total_a_payer",
        "client",
    )

    search_field = (
        "numero_contacter",
        "date_arriver",
        "heure_arriver",
        "temps_sejour",
        "chambre",
        "choixSejour",
        "total_a_payer",
        "client",
    )


