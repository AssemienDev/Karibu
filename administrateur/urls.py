from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    #Creer des urls
    
    

]

#Parametrer le chargement des médias
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)