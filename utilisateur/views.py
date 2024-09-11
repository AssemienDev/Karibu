from django.contrib.auth.hashers import make_password
from django.contrib.messages.storage import session
from django.shortcuts import render, redirect
from django.contrib import messages
from utilisateur.forms import ContactForm, ConnexionForm, InscriptionForm, PasseOublierEmailForm, PasseOublierCodeForm, \
    ChangePasseForm, ReservationChambreForm, ReservationEventForm
from utilisateur.models import Chambre, Suite, ChambreClimatisee, ChambreVentilee, Espace, Utilisateur, \
    CodeRecuperationUser
from django.core.mail import send_mail
import random
import string


# La Vue de l'acceuil
def index(request):
    # Recuperer les chambres
    chambre = Chambre.objects.filter(statutChambre='LIBRE')[:6]

    # Passer les chambres en paramètres
    context = {
        'chambre': chambre
    }

    # Afficher le template de la page d'acceuil
    return render(request, 'utilisateur/home.html', context)


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
    return render(request, 'utilisateur/contact.html', context)


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


# Profil
def profilUtilisateur(request):
    if 'emailUser' in request.session:

        client = Utilisateur.objects.get(mail_utilisateur=request.session['emailUser'])

        context = {
            'InfoClient': client
        }

        # Afficher le template de la page d'inscription
        return render(request, 'utilisateur/profilUtilisateur.html', context)

    else:
        return redirect('connexion')


# Déconnexion
def decoUtilisateur(request):
    try:
        # Supprime l'email de la session si présent
        if 'emailUser' in request.session:
            del request.session['emailUser']
    except KeyError:
        pass

        # Redirige vers la page de connexion
    return redirect('connexion')



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


def generate_random_code(length=6):
    """Génère un code aléatoire de 6 caractères (lettres majuscules et chiffres)."""
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))

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
                request.session['emailPasseOublier'] = form.cleaned_data['emailUser']

                code = generate_random_code()

                email = form.cleaned_data['email']
                try:
                    # Rechercher l'utilisateur associé à cet email
                    user = Utilisateur.objects.get(mail_utilisateur=email)
                    # Envoyer un email de réinitialisation du mot de passe

                    code_recuperation, created = CodeRecuperationUser.objects.get_or_create(client=user)

                    # Mettre à jour le code et la date de création
                    code_recuperation.code = code
                    code_recuperation.save()


                    send_mail(
                        subject='Réinitialisation du mot de passe Code',
                        message=f'Voici votre code: {code}.',
                        from_email='support@votresite.com',
                        recipient_list=[email],
                        fail_silently=False,
                    )

                    messages.success(request, 'Un email a été envoyé contenant le code pour réinitialiser votre mot de passe.')
                    # Recuperer vers la page du code
                    return redirect('passeOublierCode')  # Redirigez vers une page
                except Utilisateur.DoesNotExist:
                    messages.error(request, 'Aucun utilisateur trouvé avec cet email.')

        else:

            # Recuperer le formulaire de l'email lors du mot de passe oublier
            form = PasseOublierEmailForm()

        # Passer le form de contact en paramètres
        context = {
            'formEmail': form
        }

        # Afficher le template de la page d'email
        return render(request, 'utilisateur/passeOublierEmail.html', context)


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

                password = form.cleaned_data['password']

                # Récupérer l'utilisateur
                user = Utilisateur.objects.get(mail_utilisateur=request.session['emailPasseOublier'])
                user.mot_de_passe = make_password(password)  # Hacher le nouveau mot de passe
                user.save()

                messages.success(request, 'Votre mot de passe a été changé avec succès.')
                # Recuperer vers la page de connexion
                return redirect('connexion')

        # Recuperer le formulaire de mot de passe
        form = ChangePasseForm()

        # Passer le form de contact en paramètres
        context = {
            'formCode': form
        }
        # Afficher le template de la page de message
        return render(request, 'utilisateur/changePasse.html', context)


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
            return render(request, 'utilisateur/detailsChambre.html', context)

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
            return render(request, 'utilisateur/detailsChambreVideo.html', context)

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
                'forms': form
            }

            # Afficher le template de la page d'acceuil
            return render(request, 'utilisateur/reservationChambre.html', context)

        else:
            return redirect('chambreDisponible')
    else:
        return redirect('connexion')


# Detail de l'espace event
def espaceEvent(request):
    if Espace.objects.exists():

        # Recuperer les details de l'espace
        try:
            espace = Espace.objects.get()  # Récupère l'objet Espace unique
        except Espace.DoesNotExist:
            espace = None  # Gère le cas où l'objet n'existe pas

        # Passer l'espace en paramètre
        context = {
            'espace': espace,
        }

        # Afficher le template de la page d'acceuil
        return render(request, 'utilisateur/espaceEvenementiel.html', context)

    else:
        return redirect('acceuil')


# Réservation de la chambre disponible
def reservationEvent(request):
    if 'emailUser' in request.session:

        try:
            espace = Espace.objects.get()  # Récupère l'objet Espace unique
        except Espace.DoesNotExist:
            espace = None

            # Verifier que la requete est POST
            if request.method == 'POST':

                # Recuperer le formulaire de contact depuis la page
                form = ReservationEventForm(request.POST)

                # Valider le formulaire de reservation
                if form.is_valid():
                    pass

                    # Recuperer vers le profil du client
                    #return redirect('profilClient')

            # Recuperer le formulaire de mot de passe
            form = ReservationEventForm()

            # Passer les chambres en paramètres
            context = {
                'detailEspace': espace,
                'forms': form
            }

            # Afficher le template de la page d'acceuil
            return render(request, 'utilisateur/reservationEvent.html', context)

    else:
        return redirect('connexion')
