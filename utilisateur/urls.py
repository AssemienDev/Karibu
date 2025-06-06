from django.urls import path
from utilisateur import views

urlpatterns = [
    # Url de l'acceuil
    path('', views.index, name='index'),
    path('acceuil', views.index, name='acceuil'),

    # Url de la page d'espace evenementiel
    path('espace_event', views.espaceEvent, name='espace_event'),

    # Url de la page d'espace evenementiel salle event
    path('espace_event_salle', views.espaceEventSalleEvent, name='espace_event_salle'),

    # Url de la page d'espace evenementiel garage
    path('espace_event_garage', views.espaceEventGarage, name='espace_event_garage'),

    # Url de la page d'espace evenementiel salle vip
    path('espace_event_vip', views.espaceEventSalleVip, name='espace_event_vip'),

    # Url de la page de reservation Event
    path('reservationEvent', views.reservationEvent,
         name='reservationEvent'),

    # Url de la page de contact
    path('contact', views.contact, name='contact'),

    # Url de la page de connexion
    path('connexion', views.connexion, name='connexion'),

    # Url de la page de profil de l'utilisateur
    path('profilUtilisateur', views.profilUtilisateur, name='profil'),

    # Url de la page de déconnexion
    path('deconnexion', views.decoUtilisateur, name='deconnexion'),

    # Url de la page de suppression
    path('suppression', views.suppUtilisateur, name='suppression'),

    # Url de la page de reservation
    path('reservation', views.reservation, name='reservation'),

    # Url de la page d'insciption
    path('inscription', views.inscription, name='inscription'),

    # Url de la page du mot de passe oublier "Email"
    path('passeOublierEmail', views.passeOublierEmail, name='passeOublierEmail'),

    # Url de la page du mot de passe oublier "Code"
    path('passeOublierCode', views.passeOublierCode, name='passeOublierCode'),

    # Url de la page du mot de passe oublier "Changer mot de passe"
    path('passeOublierChangePasse', views.passeOublierChangePasse, name='passeOublierChangePasse'),

    # Url de la page de listage des chambres disponibles
    path('chambreDisponible', views.listeChambreDisponible, name='chambreDisponible'),

    # Url de la page details de la chambre
    path('detailsChambre/<int:chambre_id>', views.detailChambre, name='detailsChambre'),

    # Url de la page de reservation
    path('reservationChambre/<int:chambre_id>', views.reservationChambre,
         name='reservationChambre'),


    # Url de la page de details chambre vidéo
    path('chambreDisponible/detailsChambreVideo/<int:chambre_id>', views.detailChambreVideo,
         name='detailsChambreVideo'),


]
