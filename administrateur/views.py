from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import AjoutChambreClim,AjoutChambreVent,AjoutSuite,AjoutEspace
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
    affiche_chambre_clim = ChambreClimatisee.objects.all()
    return render(request,"admin/list_chambre_clim.html",{'affiche_clim':affiche_chambre_clim})

#la vue pour lister les chambres ventilées
def list_chambre_vent(request):
    affiche_chambre_vent = ChambreVentilee.objects.all()
    return render(request,"admin/list_chambre_vent.html",{"affiche_vent":affiche_chambre_vent})


#la vue pour lister les suites
def list_suite(request):
    affiche_suite = Suite.objects.all()
    return render(request,"admin/list_suite.html",{"affiche_suite":affiche_suite})

#la vue pour lister  les espaces
def list_espace(request):
    affiche_espace = Espace.objects.all()
    return render(request,"admin/list_espace.html",{"affiche_espace":affiche_espace})

#la vue pour lister les commandes d'espace 
def list_commande_esp(request):
    commande = CommandeEspace.objects.all()
    return render(request,"list_commande_esp.html",{"commande":commande})

#la vue pour lister les commandes de logement
def list_commande_log(request):
    logement = CommandeLogement.objects.all()
    return render(request,'list_commande_log.html',{"logement":logement})

#la vue pour ajouter une chambre
def ajout_chambre(request):

    return render(request,'ajout_chambre.html')

#la vue pour ajouter une chambre ventilee
def ajout_chambre_vent(request):
    # l'afficheur de popup
    ajouter = False

    # voir si le form est bon et valide
    if request.method == 'POST':


        form = AjoutChambreVent(request.POST, request.FILES)
        if form.is_valid():

            # recupere l'id de la chambre ajouter
            chambre = form.save()

            # l'ajouter dans chambre
            Chambre.objects.create(chambre_ventilee=chambre, statutChambre=chambre.statutChambre)

            ajouter = True

            #actualise le form
            form = AjoutChambreVent()
            
    else:
        
        form = AjoutChambreVent()
        #récuperer ces colonnes de la table
      
      
    return render(request,'ajout_chambre_vent.html',{'form':form, 'ajouter':ajouter})



#la vue pour ajouter une chambre climatisee
def ajout_chambre_clim(request):
    # voir si le form est bon et valide

    # l'afficheur de popup
    ajouter = False

    if request.method == 'POST':
        form = AjoutChambreClim(request.POST)
        if form.is_valid():

            # recupere la chambre ajouter
            chambre = form.save()

            # l'ajouter dans chambre
            Chambre.objects.create(chambre_climatisee=chambre, statutChambre=chambre.statutChambre)

            ajouter = True

            #actualise le form
            form = AjoutChambreClim()
    else:
        
        form = AjoutChambreClim()
        #récuperer ces colonnes de la table
      
      
    return render(request,'ajout_chambre_clim.html',{'form':form, 'ajouter':ajouter})



#la vue pour ajouter une suite
def ajout_suite(request):
    # l'afficheur de popup
    ajouter = False
    # voir si le form est bon et valide
    if request.method == 'POST':
        form = AjoutSuite(request.POST)
        if form.is_valid():

            # recupere la chambre ajouter
            chambre = form.save()

            # l'ajouter dans chambre
            Chambre.objects.create(suite=chambre, statutChambre=chambre.statutChambre)

            ajouter = True

            #actualise le form
            form = AjoutSuite()
    else:
        
        form = AjoutSuite()
        #récuperer ces colonnes de la table
      
      
    return render(request,'ajout_suite.html',{'form':form, 'ajouter':ajouter})



#la vue pour ajouter un espace 
def ajout_espace(request):
    # voir si le form est bon et valide
    if request.method == 'POST':
        form = AjoutEspace(request.POST)
        if form.is_valid():
            form.save()

            #actualise le form
            form = AjoutEspace()
    else:
        
        form = AjoutEspace()
        #récuperer ces colonnes de la table
      
      
    return render(request,'ajout_espace.html',{'form':form})


#la vue pour supprimer une chambre climatisée dans la bd
def supprimer(request,id):
    if request.method == 'POST':
        sup = ChambreClimatisee.objects.get(pk=id)
        sup.delete()
        return HttpResponseRedirect('/admini/ListChambreClim')

#la vue pour supprimer une chambre ventilée dans la bd
def supprimer_vent(request,id):
    if request.method == 'POST':
        sup = ChambreVentilee.objects.get(pk=id)
        sup.delete()
        return HttpResponseRedirect('/admini/ListChambreVent')

#la vue pour supprimer une suite dans la bd
def supprimer_suite(request,id):
    if request.method == 'POST':
        sup = Suite.objects.get(pk=id)
        sup.delete()
        return HttpResponseRedirect('/admini/ListSuite') 

#la vue pour supprimer un espace dans la bd
def supprimer_espace(request,id):
    if request.method == 'POST':
        sup = Espace.objects.get(pk=id)
        sup.delete()
        return HttpResponseRedirect('/admini/ListEspace')

#la vue pour modifier une chambre clim
def modifier_clim(request,id):
    if request.method == 'POST':
        mod = ChambreClimatisee.objects.get(pk=id)
        form = AjoutChambreClim(request.POST,instance=mod)
        if form.is_valid():
            form.save()
            return redirect('ListChambreClim')  # Redirection vers la liste des chambres climatisées après sauvegarde réussie
    else:
        mod = ChambreClimatisee.objects.get(pk=id)
        form = AjoutChambreClim(instance=mod)

    return render(request,'admin/modif_chambre_clim.html',{'form':form,})
    

#la vue pour modifier une chambre vent
def modifier_vent(request,id):
    if request.method == 'POST':
        mod = ChambreVentilee.objects.get(pk=id)
        form = AjoutChambreVent(request.POST,request.FILES,instance=mod)
        if form.is_valid():
            form.save()
            return redirect('ListChambreVent')  # Redirection vers la liste des chambres climatisées après sauvegarde réussie
    else:
        mod = ChambreVentilee.objects.get(pk=id)
        form = AjoutChambreVent(instance=mod)

    return render(request,'admin/modif_chambre_vent.html',{'form':form,})
    

#la vue pour modifier une suite
def modifier_suite(request,id):
    if request.method == 'POST':
        mod = Suite.objects.get(pk=id)
        form = AjoutSuite(request.POST,instance=mod)
        if form.is_valid():
            form.save()
            return redirect('ListSuite')  # Redirection vers la liste des chambres climatisées après sauvegarde réussie
    else:
        mod = Suite.objects.get(pk=id)
        form = AjoutSuite(instance=mod)

    return render(request,'admin/modif_suite.html',{'form':form,})
    
#la vue pour modifier un espace 
def modifier_espace(request,id):
    if request.method == 'POST':
        mod = Espace.objects.get(pk=id)
        form = AjoutEspace(request.POST,instance=mod)
        if form.is_valid():
            form.save()
            return redirect('ListEspace')  # Redirection vers la liste des chambres climatisées après sauvegarde réussie
    else:
        mod = Espace.objects.get(pk=id)
        form = AjoutEspace(instance=mod)

    return render(request,'admin/modif_espace.html',{'form':form,})
    