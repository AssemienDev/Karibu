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


#la vue pour ajouter une  chambre
def ajout_chambre(request):
    if request.method == "POST":
        #récupère les données envoyées par le form via les noms donnés dans le template html et les stocks dans les variables
        statutChambre == request.POST.get('statutChambre')
        chambre_climatisee == request.POST.get('chambre_climatisee') == 'on' #on est la valeur envoyée si la case est cochée
        chambre_ventilee== request.POST.get('chambre_ventilee') == 'on'
        suite == request.POST.get('suite') == 'on' 

        #creation
        Chambre.objects.create(
            statutChambre=statutChambre,
            chambre_climatisee=chambre_climatisee,
            chambre_ventilee=chambre_ventilee,
        )

         #redirection vers la liste des chambres après ajout
        return redirect('list_chambre')

    return render(request,'ajout_chambre.html')




#la vue pour ajouter une chambre ventilee
def ajout_chambre_vent(request):
    if request.method == "POST":
        #récupère les données envoyées par le form via les noms donnés dans le template html et les stocks dans les variables 
        numeroChambre = request.POST.get('NumeroChambre')
        photo1 = request.FILES.get('photo1')
        photo2 = request.FILES.get('photo2')
        photo3 = request.FILES.get('photo3')
        photo4 = request.FILES.get('photo4')
        video1 = request.FILES.get('video1')
        video2 = request.FILES.get('video2')
        video3 = request.FILES.get('video3')
        description = request.POST.get('description')
        prix_nuite = request.POST.get('prix_nuite')
        prix_journe = request.POST.get('prix_journe')


        #créer une nouvelle chambre
        ChambreVentilee.objects.Create(
            numeroChambre=numeroChambre,
            photo1=photo1,
            photo2=photo2,
            photo3=photo3,
            photo4=photo4,
            video1=video1,
            video2=video2,
            video3=video3,
            description=description,
            prix_nuite=prix_nuite,
            prix_journe=prix_journe
        )

        #redirection vers la liste des chambres après ajout
        return redirect('list_chambre_vent')

    return render(request,'ajout_chambre_vent.html')


#la vue pour ajouter une chambre climatisee
def ajout_chambre_clim(request):
    if request.method == "POST":
        #récupère les données envoyées par le form via les noms donnés dans le template html et les stocks dans les variables 
        numeroChambre = request.POST.get('NumeroChambre')
        photo1 = request.FILES.get('photo1')
        photo2 = request.FILES.get('photo2')
        photo3 = request.FILES.get('photo3')
        photo4 = request.FILES.get('photo4')
        video1 = request.FILES.get('video1')
        video2 = request.FILES.get('video2')
        video3 = request.FILES.get('video3')
        description = request.POST.get('description')
        prix_nuite = request.POST.get('prix_nuite')
        prix_journe = request.POST.get('prix_journe')


        #créer une nouvelle chambre
        ChambreVentilee.objects.Create(
            numeroChambre=numeroChambre,
            photo1=photo1,
            photo2=photo2,
            photo3=photo3,
            photo4=photo4,
            video1=video1,
            video2=video2,
            video3=video3,
            description=description,
            prix_nuite=prix_nuite,
            prix_journe=prix_journe
        )

        #redirection vers la liste des chambres après ajout
        return redirect('list_chambre_clim')

    return render(request,'ajout_chambre_clim.html')


#la vue pour ajouter une suite
def ajout_suite(request):
    if request.method == "POST":
        #récupère les données envoyées par le form via les noms donnés dans le template html et les stocks dans les variables 
        numeroChambre = request.POST.get('NumeroChambre')
        photo1 = request.FILES.get('photo1')
        photo2 = request.FILES.get('photo2')
        photo3 = request.FILES.get('photo3')
        photo4 = request.FILES.get('photo4')
        video1 = request.FILES.get('video1')
        video2 = request.FILES.get('video2')
        video3 = request.FILES.get('video3')
        description = request.POST.get('description')
        prix_nuite = request.POST.get('prix_nuite')
        prix_journe = request.POST.get('prix_journe')


        #créer une nouvelle chambre
        ChambreVentilee.objects.Create(
            numeroChambre=numeroChambre,
            photo1=photo1,
            photo2=photo2,
            photo3=photo3,
            photo4=photo4,
            video1=video1,
            video2=video2,
            video3=video3,
            description=description,
            prix_nuite=prix_nuite,
            prix_journe=prix_journe
        )

        #redirection vers la liste des chambres après ajout
        return redirect('list_suite')

    return render(request,'ajout_suite.html')


#la vue pour ajouter un espace
def ajout_espace(request):
    if request.method == "POST":
        #récupère les données envoyées par le form via les noms donnés dans le template html et les stocks dans les variables 
        numeroChambre = request.POST.get('NumeroChambre')
        photo1 = request.FILES.get('photo1')
        photo2 = request.FILES.get('photo2')
        photo3 = request.FILES.get('photo3')
        photo4 = request.FILES.get('photo4')
        photo5 = request.FILES.get('photo5')
        photo6 = request.FILES.get('photo6')
        description = request.POST.get('description')
        prix = request.POST.get('prix')


        #créer une nouvelle chambre
        ChambreVentilee.objects.Create(
            numeroChambre=numeroChambre,
            photo1=photo1,
            photo2=photo2,
            photo3=photo3,
            photo4=photo4,
            photo5=photo5,
            photo6=photo6,
            description=description,
            prix=prix
        )

        #redirection vers la liste des chambres après ajout
        return redirect('list_espace')

    return render(request,'ajout_espace.html')