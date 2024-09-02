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
    path('ListChambreClim', views.list_chambre_clim),

    #url de la liste des chambres ventilées
    path('ListChambreVent', views.list_chambre_vent),

    #url de la liste des suites
    path('ListSuite', views.list_suite),

    #url de la liste des espaces
    path('ListEspace', views.list_espace),

    #url de la liste des commandes d' espaces
    path('ListCommandeEsp', views.list_commande_esp),

    #url de la liste des commandes de logements
    path('ListCommandeLog', views.list_commande_log),



    

]

#Parametrer le chargement des médias
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)