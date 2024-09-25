import random
import string

from django.shortcuts import render,HttpResponseRedirect,redirect,get_object_or_404
from django.contrib import messages

from espaceKaribu import settings
from .forms import AjoutChambreClim, AjoutChambreVent, AjoutSuite, AjoutEspace, ConnexionForm, ConnexionCodeForm
from utilisateur.models import Utilisateur, Chambre, ChambreClimatisee, ChambreVentilee, Suite, Espace, CommandeEspace, \
    CommandeLogement, Administrateur, CodeConnexionAdmin,ContactAdmin
#L'envoi d'email avec django
from django.core.mail import send_mail


# Envoi d'email
def envoyer_email(recepteur, subject, message):
    if isinstance(recepteur, str):
        recepteur = [recepteur]  # Convertit la chaîne de caractères en liste

    try:
        envoi = send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recepteur)
        print("Email envoyé, statut:", envoi)
    except Exception as e:
        print("Erreur lors de l'envoi de l'email:", e)

# Create your views here.


#je mets directement le contexte dedans

#la vue pour récuperer la liste des utilisateurs
def list_user (request):
    if "emailAdmin" in request.session:
        user = Utilisateur.objects.all()
        return render (request, "admin/list_user.html",{'utilisateur':user})
    else:
        return redirect('connexionAdmin')

#la vue pour récuperer la commande de l'espace
def list_cmde_espace (request):
    if "emailAdmin" in request.session:
        cmde_espace = CommandeEspace.objects.all()
        return render (request, "admin/list_cmde_espace.html",{'cmde_espace':cmde_espace})
    else:
        return redirect('connexionAdmin')


#la vue pour récuperer la liste des contacts de l'admin
def list_contact_admin (request):
    if "emailAdmin" in request.session:
        if ContactAdmin.objects.exists():
            contact_admin = ContactAdmin.objects.all()
        else:
            contact_admin = None
        return render (request, "admin/list_contact_admin.html",{'contact_admin':contact_admin})
    else:
        return redirect('connexionAdmin')






#la vue pour lister les chambres climatisées
def list_chambre_clim(request):
    if "emailAdmin" in request.session:
        affiche_chambre_clim = ChambreClimatisee.objects.all()
        return render(request,"admin/list_chambre_clim.html",{'affiche_clim':affiche_chambre_clim})
    else:
        return redirect('connexionAdmin')

#la vue pour lister les chambres ventilées
def list_chambre_vent(request):
    if "emailAdmin" in request.session:
        affiche_chambre_vent = ChambreVentilee.objects.all()
        return render(request,"admin/list_chambre_vent.html",{"affiche_vent":affiche_chambre_vent})
    else:
        return redirect('connexionAdmin')


#la vue pour lister les suites
def list_suite(request):
    if "emailAdmin" in request.session:
        affiche_suite = Suite.objects.all()
        return render(request,"admin/list_suite.html",{"affiche_suite":affiche_suite})
    else:
        return redirect('connexionAdmin')

#la vue pour lister  les espaces
def list_espace(request):
    if "emailAdmin" in request.session:
        affiche_espace = Espace.objects.all()
        return render(request,"admin/list_espace.html",{"affiche_espace":affiche_espace})
    else:
        return redirect('connexionAdmin')

#la vue pour lister les commandes d'espace 
def list_commande_esp(request):
    if "emailAdmin" in request.session:
        affiche_commande_esp = CommandeEspace.objects.all()
        return render(request,"admin/list_cmde_espace.html",{"affiche_commande_esp":affiche_commande_esp})
    else:
        return redirect('connexionAdmin')

#la vue pour lister les commandes de logement
def list_commande_log(request):
    if "emailAdmin" in request.session:
        affiche_cmde_log = CommandeLogement.objects.all()
        return render(request,'list_cmde_logement.html',{"affiche_cmde_log":affiche_cmde_log})
    else:
        return redirect('connexionAdmin')

#la vue pour ajouter une chambre
def ajout_chambre(request):
    if "emailAdmin" in request.session:
        return render(request,'ajout_chambre.html')
    else:
        return redirect('connexionAdmin')

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
        form = AjoutChambreClim(request.POST,request.FILES)
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
        form = AjoutSuite(request.POST,request.FILES)
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
    # Vérifier si un espace existe déjà
    espace_existant = Espace.objects.exists()
    if espace_existant:
        # Message d'erreur si un espace existe déjà
        messages.error(request, "Un espace existe déjà. Vous ne pouvez pas en ajouter un autre.")
        return redirect('ListEspace')  # Rediriger vers la page de liste des espaces


    # voir si le form est bon et valide
    if request.method == 'POST':
        form = AjoutEspace(request.POST,request.FILES)
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

#la vue pour validé une commande espace
def valider_commande(request, id):
    cmde_espace = get_object_or_404(CommandeEspace, id=id)
    cmde_espace.etat_commande = 'validee'
    cmde_espace.save()

    # Mettre à jour le statut de l'espace
    # Accéder à l'espace associé à cette commande
    espace = cmde_espace.espace  #  accédez à l'espace lié à la commande

    # Modifier le statut de l'espace
    espace.statutEspace = 'occupé'
    espace.save()  # Sauvegarder les modifications de l'espace
    return redirect('ListCommandeEsp')

def refuser_commande(request, id):
    cmde_espace = get_object_or_404(CommandeEspace, id=id)
    cmde_espace.etat_commande = 'refusee'
    cmde_espace.delete()
    return redirect('ListCommandeEsp')

    
#la vue pour supprimer une comande d'espace
def supprimer_cmde_espace(request, id):
    # Récupérer l'instance de la commande
    cmde_espace = get_object_or_404(CommandeEspace, id=id)

    # Accéder à l'espace associé à cette commande
    espace = cmde_espace.espace

    # Modifier le statut de l'espace
    espace.statutEspace = 'libre'
    espace.save()  # Sauvegarder les modifications de l'espace

    # Supprimer la commande
    cmde_espace.delete()

    return redirect('ListCommandeEsp')



#la vue pour validé une commande logement
def valider_commande_log(request, id):
    cmde_logement = get_object_or_404(CommandeLogement, id=id)
    cmde_logement.etat_commande = 'validee'
    cmde_logement.save()

    # Accéder à l'espace (logement) associé à cette commande
    logement = cmde_logement.chambre  # accédez à la chambre liée à la commande

    # Modifier le statut de la chambre
    logement.statutChambre = 'occupé'

    # Vérifier quel type de chambre est associé et mettre à jour le statut
    if logement.chambre_climatisee:
        print("Chambre climatisée trouvée")
        logement.chambre_climatisee.statutChambre = 'occupé'
        logement.chambre_climatisee.save()
    elif logement.chambre_ventilee:
        print("Chambre ventilée trouvée")
        logement.chambre_ventilee.statutChambre = 'occupé'
        logement.chambre_ventilee.save()
    elif logement.suite:
        print("Suite trouvée")
        logement.suite.statutChambre = 'occupé'
        logement.suite.save()

    # Sauvegarder les modifications de la chambre
    logement.save()

    return redirect('ListCommandeLog')


def refuser_commande_log(request, id):
    cmde_logement = get_object_or_404(CommandeLogement, id=id)
    cmde_logement.etat_commande = 'refusee'
    cmde_logement.delete()
    return redirect('ListCommandeLog')

    
#la vue pour supprimer une comande de logement
def supprimer_cmde_logement(request, id):
    # Récupérer l'instance de la commande
    cmde_logement = get_object_or_404(CommandeLogement, id=id)

    # Accéder à l'espace associé à cette commande
    logement = cmde_logement.chambre

    # Modifier le statut de l'espace
    logement.statutChambre = 'libre'
    logement.save()  # Sauvegarder les modifications de l'espace

    # Vérifier quel type de chambre est associé et mettre à jour le statut
    if logement.chambre_climatisee:
        print("Chambre climatisée trouvée")
        logement.chambre_climatisee.statutChambre = "libre"
        logement.chambre_climatisee.save()
    elif logement.chambre_ventilee:
        print("Chambre ventilée trouvée")
        logement.chambre_ventilee.statutChambre = 'libre'
        logement.chambre_ventilee.save()
    elif logement.suite:
        print("Suite trouvée")
        logement.suite.statutChambre = 'libre'
        logement.suite.save()

    # Supprimer la commande
    cmde_logement.delete()

    return redirect('ListCommandeLog')



#Connexion Admin
def connexionAdmin(request):
    if 'emailAdmin' in request.session:
        return redirect('ListUser')
    else:
        # Verifier que la requete est POST
        if request.method == 'POST':

            # Recuperer le formulaire de contact depuis la page
            form = ConnexionForm(request.POST)

            # Valider le formulaire de contact
            if form.is_valid():
                request.session['emailPasAdmin'] = form.cleaned_data['email']
                code = generate_random_code()

                try:
                    # Rechercher l'utilisateur associé à cet email
                    admini = Administrateur.objects.get(mail_admin=request.session['emailPasAdmin'])
                    # Envoyer un email de réinitialisation du mot de passe

                    code_validation, created = CodeConnexionAdmin.objects.get_or_create(admin=admini)

                    # Mettre à jour le code et la date de création
                    code_validation.code = code
                    code_validation.save()

                    sujet = "Code de connexion de l'administrateur"
                    message = (
                        f"Bonjour/Bonsoir, Voici votre code: {code}.")
                    envoyer_email(request.session['emailPasAdmin'], sujet, message)

                    messages.success(request,
                                     'Un email a été envoyé contenant le code pour la connexion votre mot de passe.')
                    # Recuperer vers le code de connexion
                    return redirect('codeConnexionAdmin')
                except:
                    None

        # Recuperer le formulaire de connexion
        form = ConnexionForm()

        # Passer le form de contact en paramètres
        context = {
            'formConnexion': form
        }

        # Afficher le template de la page de connexion
        return render(request, 'admin/connexionAdmin.html', context)


def generate_random_code(length=6):
    """Génère un code aléatoire de 6 caractères (lettres majuscules et chiffres)."""
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))


# La Vue du Code de connexion de l'admin
def connexionAdminCode(request):
    if 'emailPasAdmin' not in request.session:
        return redirect('connexionAdmin')
    else:
        # Verifier que la requete est POST
        if request.method == 'POST':

            # Recuperer le formulaire de contact depuis la page
            form = ConnexionCodeForm(request.POST, request)

            # Valider le formulaire de code
            if form.is_valid():

                admini = Administrateur.objects.get(mail_admin=request.session['emailPasAdmin'])

                if form.cleaned_data['code'] == CodeConnexionAdmin.objects.get(admin=admini).code:
                    request.session['emailAdmin'] = request.session['emailPasAdmin']

                    del request.session['emailPasAdmin']

                    # Recuperer vers la page changé mot de passe
                    return redirect('ListUser')

        # Recuperer le formulaire du code lors du mot de passe oublier
        form = ConnexionCodeForm()

        # Passer le form de contact en paramètres
        context = {
            'formCode': form
        }

        # Afficher le template de la page de code
        return render(request, 'admin/connexionCode.html', context)


    
#la vue pour la deconnexion de l'admin
def AdminDeconnexion(request):
    try:
        # Supprime l'email de la session si présent
        if 'emailUser' in request.session:
            del request.session['emailAdmin']
    except KeyError:
        pass

        # Redirige vers la page de connexion de l'Admin
    return redirect('connexionAdmin')
