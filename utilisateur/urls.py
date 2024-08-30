from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from utilisateur import views

urlpatterns = [
    # Url de l'acceuil
    path('', views.index, name='index'),
    path('acceuil', views.index, name='index'),

    # Url de la page de contact
    path('contact', views.contact, name='contact'),

    # Url de la page de connexion
    path('connexion', views.connexion, name='connexion'),

    # Url de la page du mot de passe oublier "Email"
    path('passeOublierEmail', views.passeOublierEmail, name='passeOublier'),

    # Url de la page du mot de passe oublier "Code"
    path('passeOublierCode', views.passeOublierCode, name='passeOublier'),

    # Url de la page de listage des chambres disponibles
    path('chambreDisponible', views.listeChambreDisponible, name='chambreDisponible'),
]

#Parametrer le chargement des médias
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)