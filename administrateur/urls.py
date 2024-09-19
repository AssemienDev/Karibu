from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from administrateur import views


urlpatterns = [
    #Creer des urls

    #url de la liste des utilisateurs
    path('ListUser', views.list_user),

    #url de la liste des chambres
    path('ListChambre', views.list_chambre),

    #url de la liste des chambres climatisées
    path('ListChambreClim', views.list_chambre_clim,name="ListChambreClim"),

    #url de la liste des chambres ventilées
    path('ListChambreVent', views.list_chambre_vent,name='ListChambreVent'),

    #url de la liste des suites
    path('ListSuite', views.list_suite,name='ListSuite'),

    #url de la liste des espaces
    path('ListEspace', views.list_espace,name="ListEspace"),

    #url de la liste des commandes d' espaces
    path('ListCommandeEsp', views.list_commande_esp),

    #url de la liste des commandes de logements
    path('ListCommandeLog', views.list_commande_log),

     #url pour l'ajout des chambres
    path('AjoutChambre',views.ajout_chambre),

    #url pour l'ajout des chambres ventilees
    path('AjoutChambreVent',views.ajout_chambre_vent),

    #url pour l'ajout des chambres  climatisees
    path('AjoutChambreClim',views.ajout_chambre_clim),

    #url pour l'ajout des suites
    path('AjoutSuite',views.ajout_suite),

    #url pour l'ajout des espaces
    path('AjoutEspace',views.ajout_espace),

    #url pour supprimer une chambre climatisee
    path('Supprimer/<int:id>',views.supprimer,name="supprimer"),

    #url pour supprimer une chambre Ventilee
    path('supprimer_vent/<int:id>',views.supprimer_vent,name="supprimer_vent"),

    #url pour supprimer une suite
    path('supprimer_suite/<int:id>',views.supprimer_suite,name="supprimer_suite"),

    #url pour supprimer un espace
    path('supprimer_espace/<int:id>',views.supprimer_espace,name="supprimer_espace"),




    # URL pour modifier une chambre climatisée
    path('modifier_clim/<int:id>/', views.modifier_clim, name='modifier'),

    # URL pour modifier une chambre ventilée
    path('modifier_vent/<int:id>/', views.modifier_vent, name='modifier_vent'),

    # URL pour modifier une suite
    path('modifier_suite/<int:id>/', views.modifier_suite, name='modifier_suite'),

    # URL pour modifier un espace
    path('modifier_espace/<int:id>/', views.modifier_espace, name='modifier_espace'),

    

]

#Parametrer le chargement des médias
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)