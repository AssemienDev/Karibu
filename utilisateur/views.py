from django.contrib.messages.storage import session
from django.shortcuts import render, redirect

from utilisateur.forms import ContactForm, ConnexionForm, InscriptionForm, PasseOublierEmailForm, PasseOublierCodeForm, \
    ChangePasseForm, ReservationChambreForm
from utilisateur.models import Chambre, Suite, ChambreClimatisee, ChambreVentilee, Espace


# La Vue de l'acceuil
def index(request):
    # Recuperer les chambres
    chambre = Chambre.objects.filter(statutChambre='LIBRE')[:6]

    # Passer les chambres en paramètres
    context = {
        'chambre': chambre
    }

    # Afficher le template de la page d'acceuil
    return render(request,'utilisateur/home.html',context)


# La Vue du contact
def contact(request):
    # Verifier que la requete est POST
    if request.method == 'POST':

        # Recuperer le formulaire de contact depuis la page
        form = ContactForm(request.POST)

        # Valider le formulaire de contact
        if form.is_valid():

            form.save()
            # Recuperer vers la page d'Acceuil
            return redirect('acceuil')

    # Recuperer le formulaire de contact
    form = ContactForm()

    # Passer le form de contact en paramètres
    context = {
        'formContact': form
    }

    # Afficher le template de la page de contact
    return render(request,'utilisateur/contact.html',context)


# La Vue de connexion
def connexion(request):
    if 'emailUser' in request.session:
        return redirect('acceuil')
    else:
        # Verifier que la requete est POST
        if request.method == 'POST':

            # Recuperer le formulaire de contact depuis la page
            form = ConnexionForm(request.POST)

            # Valider le formulaire de contact
            if form.is_valid():

                request.session['emailUser'] = form.cleaned_data['emailUser']

                # Recuperer vers la page de profil
                # return redirect('acceuil')

        # Recuperer le formulaire de connexion
        form = ConnexionForm()

        # Passer le form de contact en paramètres
        context = {
            'formConnexion': form
        }

        # Afficher le template de la page de connexion
        return render(request, 'utilisateur/connexion.html', context)


# La Vue d'inscription
def inscription(request):
    if 'emailUser' in request.session:
        return redirect('acceuil')
    else:
        # Verifier que la requete est POST
        if request.method == 'POST':

            # Recuperer le formulaire de contact depuis la page
            form = InscriptionForm(request.POST)

            # Valider le formulaire de contact
            if form.is_valid():

                form.save()

                # Recuperer vers la page d'Acceuil
                return redirect('connexion')

        # Recuperer le formulaire d'inscription
        form = InscriptionForm()

        # Passer le form de contact en paramètres
        context = {
            'formInscription': form
        }

        # Afficher le template de la page d'inscription
        return render(request, 'utilisateur/inscription.html', context)


# La Vue du passe oublié Email
def passeOublierEmail(request):
    if 'emailUser' in request.session:
        return redirect('acceuil')
    else:
        # Verifier que la requete est POST
        if request.method == 'POST':

            # Recuperer le formulaire de contact depuis la page
            form = PasseOublierEmailForm(request.POST)

            # Valider le formulaire de l'email oublier
            if form.is_valid():
                # request.session['emailPasseOublier'] = form.cleaned_data['emailUser']

                # Recuperer vers la page du code
                return redirect('passeOublierCode')

        # Recuperer le formulaire de l'email lors du mot de passe oublier
        form = PasseOublierEmailForm()

        # Passer le form de contact en paramètres
        context = {
            'formEmail': form
        }

        # Afficher le template de la page d'email
        return render(request, 'passeOublierEmail.html', context)


# La Vue du passe oublié Code
def passeOublierCode(request):
    if 'emailUser' in request.session:
        return redirect('acceuil')
    else:
        # Verifier que la requete est POST
        if request.method == 'POST':

            # Recuperer le formulaire de contact depuis la page
            form = PasseOublierCodeForm(request.POST, request)

            # Valider le formulaire de code
            if form.is_valid():
                # Recuperer vers la page changer mot de passe
                return redirect('passeOublierChangePasse')

        # Recuperer le formulaire du code lors du mot de passe oublier
        form = PasseOublierCodeForm()

        # Passer le form de contact en paramètres
        context = {
            'formCode': form
        }

        # Afficher le template de la page de code
        return render(request, 'passeOublierCode.html', context)


# La Vue du message
def passeOublierChangePasse(request):
    if 'emailUser' in request.session:
        return redirect('acceuil')
    else:
        # Verifier que la requete est POST
        if request.method == 'POST':

            # Recuperer le formulaire de contact depuis la page
            form = ChangePasseForm(request.POST, request)

            # Valider le formulaire du mot de passe oublier
            if form.is_valid():
                # Recuperer vers la page de connexion
                return redirect('connexion')

        # Recuperer le formulaire de mot de passe
        form = ChangePasseForm()

        # Passer le form de contact en paramètres
        context = {
            'formCode': form
        }
        # Afficher le template de la page de message
        return render(request,'changePasse.html', context)


# La Vue des chambres disponibles
def listeChambreDisponible(request):
    # Recuperer les chambres
    chambre = Chambre.objects.filter(statutChambre='LIBRE')

    # Passer les chambres en paramètres
    context = {
        'chambres': chambre
    }

    # Afficher le template de la page d'acceuil
    return render(request, 'utilisateur/chambresDisponible.html', context)


# Detail de la chambre disponible
def detailChambre(request, chambre_id):
    if 'emailUser' in request.session:

        if Chambre.objects.filter(id=chambre_id).exists():

            # Recuperer la chambre précise
            chambre = Chambre.objects.filter(id=chambre_id)

            if chambre:
                if chambre.suite:
                    # Recuperer les suites
                    chambres = Suite.objects.all()
                elif chambre.chambre_climatisee:
                    # Recuperer les chambres climatisées
                    chambres = ChambreClimatisee.objects.all()
                elif chambre.chambre_ventilee:
                    # Recuperer les chambres ventilées
                    chambres = ChambreVentilee.objects.all()

            # Passer les chambres en paramètres
            context = {
                'detailChambre': chambre,
                'chambres': chambres
            }

            # Afficher le template de la page d'acceuil
            return render(request, 'detailsChambre.html', context)

        else:
           return redirect('chambreDisponible')
    else:
        return redirect('connexion')


# Detail de la chambre disponible avec vidéo
def detailChambreVideo(request, chambre_id):
    if 'emailUser' in request.session:

        if Chambre.objects.filter(id=chambre_id).exists():

            # Recuperer la chambre précise
            chambre = Chambre.objects.filter(id=chambre_id)

            # Passer les chambres en paramètres
            context = {
                'detailChambre': chambre,
            }

            # Afficher le template de la page d'acceuil
            return render(request, 'detailsChambreVideo.html', context)

        else:
           return redirect('chambreDisponible')
    else:
        return redirect('connexion')


# Réservation de la chambre disponible
def reservationChambre(request, chambre_id):
    if 'emailUser' in request.session:

        if Chambre.objects.filter(id=chambre_id).exists():

            # Recuperer la chambre précise
            chambre = Chambre.objects.filter(id=chambre_id)

            # Verifier que la requete est POST
            if request.method == 'POST':

                # Recuperer le formulaire de contact depuis la page
                form = ReservationChambreForm(request.POST)

                # Valider le formulaire de reservation
                if form.is_valid():
                    pass

                    # Recuperer vers le profil du client
                    #return redirect('profilClient')

            # Recuperer le formulaire de mot de passe
            form = ReservationChambreForm()

            # Passer les chambres en paramètres
            context = {
                'detailChambre': chambre,
                'forms':form
            }

            # Afficher le template de la page d'acceuil
            return render(request, 'reservationChambre.html', context)

        else:
           return redirect('chambreDisponible')
    else:
        return redirect('connexion')



# Detail de l'espace event
def espaceEvent(request):
    if Espace.objects.exists():

        # Recuperer les details de l'espace
        espaces = Espace.objects.all()

        # Passer l'espace en paramètre
        context = {
            'espace': espaces,
        }

        # Afficher le template de la page d'acceuil
        return render(request, 'espace_evenementiel.html', context)

    else:
        return redirect('acceuil')


