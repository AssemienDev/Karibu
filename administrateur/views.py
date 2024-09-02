from django.shortcuts import render
from utilisateur.models import Utilisateur,Chambre,ChambreClimatisee,ChambreVentilee,Suite,Espace,CommandeEspace,CommandeLogement

# Create your views here.


#je mets directement le contexte dedans

#la vue pour récuperer la liste des utilisateurs
def list_user (request):
    user = Utilisateur.objects.all()
    return render (request, "liste_user.html",{'utilisateur':user})


#la vue pour lister les chambres
def list_chambre(request):
    chambre = Chambre.objects.all()
    return render(request,"liste_chambre.html",{"chambre":chambre})


#la vue pour lister les chambres climatisées
def list_chambre_clim(request):
    chambre_clim = ChambreClimatisee.objects.values("numeroChambre","description","prix_nuite","prix_journee")
    return render(request,"list_chambre_clim.html",{"chambre_clim":chambre_clim})

#la vue pour lister les chambres ventilées
def list_chambre_vent(request):
    chambre_vent = ChambreVentilee.objects.values("numeroChambre","description","prix_nuite","prix_journe")
    return render(request,"list_chambre_vent.html",{"chambre_vent":chambre_vent})


#la vue pour lister les suites
def list_suite(request):
    suite = Suite.objects.values("numeroChambre","description","prix_nuite","prix_journe")
    return render(request,"list_suite.html",{"suite":suite})

#la vue pour lister  les espaces
def list_espace(request):
    espace = Espace.objects.values("numeroChambre","description","prix")
    return render(request,"list_espace.html",{"espace":espace})

#la vue pour lister les commandes d'espace 
def list_commande_esp(request):
    commande = CommandeEspace.objects.all()
    return render(request,"list_commande_esp.html",{"commande":commande})

#la vue pour lister les commandes de logement
def list_commande_log(request):
    logement = CommandeLogement.objects.all()
    return render(request,'list_commande_log.html',{"logement":logement})
