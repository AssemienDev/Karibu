from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from administrateur import views


urlpatterns = [
    #Creer des urls

    #url de la liste des utilisateurs
    path('ListUser', views.list_user,name="ListUser"),

    #url de la liste des chambres climatisées
    path('ListChambreClim', views.list_chambre_clim,name="ListChambreClim"),

    #url de la liste des chambres ventilées
    path('ListChambreVent', views.list_chambre_vent,name='ListChambreVent'),

    #url de la liste des suites
    path('ListSuite', views.list_suite,name='ListSuite'),

    #url de la liste des espaces
    path('ListEspace', views.list_espace,name="ListEspace"),

    #url de la liste des commandes d' espaces
    path('ListCommandeEsp', views.list_commande_esp,name="ListCommandeEsp"),

    #url de la liste des commandes de logements
    path('ListCommandeLog', views.list_commande_log,name="ListCommandeLog"),



     #url pour l'ajout des chambres
    path('AjoutChambre',views.ajout_chambre),

    #url pour l'ajout des chambres ventilees
    path('AjoutChambreVent',views.ajout_chambre_vent,name='AjoutChambreVent'),

    #url pour l'ajout des chambres  climatisees
    path('AjoutChambreClim',views.ajout_chambre_clim,name='AjoutChambreClim'),

    #url pour l'ajout des suites
    path('AjoutSuite',views.ajout_suite,name='AjoutSuite'),

    #url pour l'ajout des espaces
    path('AjoutEspace',views.ajout_espace,name='AjoutEspace'),

    #url pour supprimer une chambre climatisee
    path('Supprimer/<int:id>',views.supprimer,name="supprimer"),

    #url pour supprimer une chambre Ventilee
    path('supprimer_vent/<int:id>',views.supprimer_vent,name="supprimer_vent"),

    #url pour supprimer une suite
    path('supprimer_suite/<int:id>',views.supprimer_suite,name="supprimer_suite"),

    #url pour supprimer un espace
    path('supprimer_espace/<int:id>',views.supprimer_espace,name="supprimer_espace"),

    #url pour supprimer une commande espace
    path('supprimer_cmde_espace/<int:id>',views.supprimer_cmde_espace,name="supprimer_cmde_espace"),

    #url pour supprimer une commande logement
    path('supprimer_cmde_logement/<int:id>',views.supprimer_cmde_logement,name="supprimer_cmde_logement"),




    # URL pour modifier une chambre climatisée
    path('modifier_clim/<int:id>/', views.modifier_clim, name='modifier'),

    # URL pour modifier une chambre ventilée
    path('modifier_vent/<int:id>/', views.modifier_vent, name='modifier_vent'),

    # URL pour modifier une suite
    path('modifier_suite/<int:id>/', views.modifier_suite, name='modifier_suite'),

    # URL pour modifier un espace
    path('modifier_espace/<int:id>/', views.modifier_espace, name='modifier_espace'),

    #url pour lister commande espace
    path('ListCmdeEspace',views.list_commande_esp,name='ListCmdeEspace'),

    # URL pour valider une commande espace
    path('valider_commande/<int:id>/', views.valider_commande, name='valider_commande'),

    # URL pour valider une commande logement
    path('valider_commande_log/<int:id>/', views.valider_commande_log, name='valider_commande_log'),

    # URL pour réfuser une commande espace
    path('refuser_commande/<int:id>/', views.refuser_commande, name='refuser_commande'),

    # URL pour réfuser une commande logement
    path('refuser_commande_log/<int:id>/', views.refuser_commande_log, name='refuser_commande_log'),



    # url de connexion de l'admin
    path('connexionAdmin', views.connexionAdmin, name="connexionAdmin"),

    path('', views.connexionAdmin, name="connexionAdmin"),

    # url de la liste des utilisateurs
    path('codeConnexionAdmin', views.connexionAdminCode, name="codeConnexionAdmin"),
    
    # url de connexion de l'admin
    path('deconnexionAdmin', views.AdminDeconnexion, name="deconnexionAdmin"),

    # url de contact de l'admin
    path('ListContactAdmin', views.list_contact_admin, name="ListContactAdmin"),
    

]

#Parametrer le chargement des médias
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)