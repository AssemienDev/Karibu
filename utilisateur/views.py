from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages

from espaceKaribu import settings
from utilisateur.forms import ContactForm, ConnexionForm, InscriptionForm, PasseOublierEmailForm, PasseOublierCodeForm, \
    ChangePasseForm, ReservationChambreForm, ReservationEventForm, ModifNameForm, ModifPasseForm
from utilisateur.models import Chambre, Suite, ChambreClimatisee, ChambreVentilee, Espace, Utilisateur, \
    CodeRecuperationUser, CommandeLogement, CommandeEspace
import random
import string

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


# La Vue de l'acceuil
def index(request):
    # Recuperer les chambres
    chambres = Chambre.objects.filter(statutChambre='libre')[:6]

    chambres_data = []
    for chambre in chambres:
        type_chambre = ''
        chambrer = None

        if chambre.suite:
            type_chambre = 'suite'
            chambrer = chambre.suite
        elif chambre.chambre_climatisee:
            type_chambre = 'chambre_climatisee'
            chambrer = chambre.chambre_climatisee
        elif chambre.chambre_ventilee:
            type_chambre = 'chambre_ventilee'
            chambrer = chambre.chambre_ventilee

        chambres_data.append({
            'idChambre': chambre,
            'chambre': chambrer,         # Add the correct related room instance
            'type_chambre': type_chambre  # Add the type for display
        })

    # Pass the chambres_data to your template
    context = {
        'chambres_data': chambres_data
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

            sujet = "MESSAGE D'INFORMATION"
            message = (
                f"Bonjour/Bonsoir, Nous avons bien réçu votre message.")
            envoyer_email(form.cleaned_data['email'], sujet, message)

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
                request.session['emailUser'] = form.cleaned_data['email']
                # Recuperer vers la page de profil
                return redirect('acceuil')

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

        if request.method == 'POST':

            formName = ModifNameForm(request.POST)
            formPasse = ModifPasseForm(request.POST, user=client)

            if formName.is_valid():

                name = formName.cleaned_data['nom']
                client.nom_complet = name
                client.save()

            if formPasse.is_valid():

                passeNew = formPasse.cleaned_data['new_password']
                client.mot_de_passe = make_password(passeNew)  # Hacher le nouveau mot de passe
                client.save()

                sujet = "Réinitialisation du mot de passe"
                message = (
                    "Bonjour/Bonsoir, Votre mot de passe a été modifié avec succès.")
                envoyer_email(client.mail_utilisateur, sujet, message)

        else:
            formName = ModifNameForm()
            formPasse = ModifPasseForm()

        context = {
            'InfoClient': client,
            'form1': formName,
            'form2': formPasse
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


# Déconnexion
def suppUtilisateur(request):
    try:
        # Supprime l'email de la session si présent
        if 'emailUser' in request.session:

            Utilisateur.objects.get(mail_utilisateur=request.session['emailUser']).delete()

            sujet = "MESSAGE D'INFORMATION"
            message = (
                f"Bonjour/Bonsoir, Vous avez supprimé votre compte.")
            envoyer_email(request.session['emailUser'], sujet, message)

            del request.session['emailUser']

    except KeyError:
        pass

        # Redirige vers la page d'inscription
    return redirect('inscription')


# Detail de l'espace event
def reservation(request):
    if 'emailUser' in request.session:

        # Récupérer l'utilisateur connecté
        client = Utilisateur.objects.get(mail_utilisateur=request.session['emailUser'])

        try:
            # Récupérer les réservations de chambres pour ce client
            reservChambre = CommandeLogement.objects.filter(client=client)

            chambres = []  # Liste pour stocker les chambres récupérées
            total_chambres = 0 # Variable pour stocker le total des réservations de chambres

            # Parcourir toutes les réservations de chambres pour ce client
            for reservation in reservChambre:
                chambrer = None
                details_chambre = {
                    'photo_chambre' : None,
                    'date_arrivee': reservation.date_arriver,
                    'heure_arrivee': reservation.heure_arriver,
                    'total': reservation.total_a_payer,
                    'etat' : reservation.etat_commande
                }

                # Vérifier le type de chambre réservée (suite, climatisée, ventilée)
                if reservation.chambre.suite:
                    chambrer = reservation.chambre.suite
                    details_chambre['photo_chambre'] = chambrer.photo1
                elif reservation.chambre.chambre_climatisee:
                    chambrer = reservation.chambre.chambre_climatisee
                    details_chambre['photo_chambre'] = chambrer.photo1
                elif reservation.chambre.chambre_ventilee:
                    chambrer = reservation.chambre.chambre_ventilee
                    details_chambre['photo_chambre'] = chambrer.photo1

                # Si une chambre est trouvée, l'ajouter à la liste des chambres avec ses détails
                if chambrer:
                    chambres.append(details_chambre)

        except CommandeLogement.DoesNotExist:
            reservChambre = None
            chambres = []
            total_chambres = 0  # Aucun total si aucune chambre n'est réservée

        try:
            # Récupérer les réservations d'espaces pour ce client
            reservEspace = CommandeEspace.objects.filter(client=client)

            espacer = []  # Liste pour stocker les espaces récupérés

            # Parcourir toutes les réservations d'espaces pour ce client
            for reservation in reservEspace:
                espaceNew = reservation.espace
                details_espace = {
                    'espace': espaceNew,
                    'date_arrivee': reservation.date_arriver,
                    'etat' : reservation.etat_commande
                }

                espacer.append(details_espace)  # Ajouter les détails de l'espace à la liste
        except CommandeEspace.DoesNotExist:
            reservEspace = None
            espacer = []

        # Passer les informations en paramètre au template
        context = {
            'reservChambres': chambres,
            'reservEspaces': espacer,
        }

        # Afficher le template de la page des réservations
        return render(request, 'utilisateur/reservations.html', context)

    else:
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

                sujet = "MESSAGE D'INFORMATION"
                message = (
                    f"Bonjour/Bonsoir, Votre inscription a bien été validé.")
                envoyer_email(form.cleaned_data['email'], sujet, message)

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

                    sujet = "Réinitialisation du mot de passe Code"
                    message = (
                        f"Bonjour/Bonsoir, Voici votre code: {code}.")
                    envoyer_email(email, sujet, message)

                    messages.success(request,
                                     'Un email a été envoyé contenant le code pour réinitialiser votre mot de passe.')
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

                client = Utilisateur.objects.get(mail_utilisateur=request.session['emailPasseOublier'])

                if form.cleaned_data['code'] == CodeRecuperationUser.objects.get(client=client).code:

                    # Recuperer vers la page changé mot de passe
                    return redirect('passeOublierChangePasse')

        # Recuperer le formulaire du code lors du mot de passe oublier
        form = PasseOublierCodeForm()

        # Passer le form de contact en paramètres
        context = {
            'formCode': form
        }

        # Afficher le template de la page de code
        return render(request, 'utilisateur/passeOublierCode.html', context)


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

                sujet = "Réinitialisation du mot de passe"
                message = (
                    f"Bonjour/Bonsoir, Votre mot de passe a été modifié avec succès.")
                envoyer_email(request.session['emailPasseOublier'], sujet, message)

                del request.session['emailPasseOublier']

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
    chambres = Chambre.objects.filter(statutChambre='libre')

    chambres_data = []
    for chambre in chambres:
        type_chambre = ''
        chambrer = None

        if chambre.suite:
            type_chambre = 'suite'
            chambrer = chambre.suite
        elif chambre.chambre_climatisee:
            type_chambre = 'chambre_climatisee'
            chambrer = chambre.chambre_climatisee
        elif chambre.chambre_ventilee:
            type_chambre = 'chambre_ventilee'
            chambrer = chambre.chambre_ventilee

        chambres_data.append({
            'idChambre': chambre,
            'chambre': chambrer,         # Add the correct related room instance
            'type_chambre': type_chambre  # Add the type for display
        })

    # Pass the chambres_data to your template
    context = {
        'chambres_data': chambres_data
    }

    # Afficher le template de la page d'acceuil
    return render(request, 'utilisateur/chambresDisponible.html', context)


# Detail de la chambre disponible
def detailChambre(request, chambre_id):

        if Chambre.objects.filter(id=chambre_id).exists():

            # Recuperer la chambre précise
            chambre = Chambre.objects.get(id=chambre_id)
            chambrer = None
            chambres = None
            typeChambre = None

            if chambre:
                if chambre.suite:
                    # Recuperer les suites
                    chambrer = chambre.suite
                    typeChambre = "SUITE"
                    chambres = Suite.objects.all()
                elif chambre.chambre_climatisee:
                    # Recuperer les chambres climatisées
                    chambrer = chambre.chambre_climatisee
                    typeChambre = "CHAMBRE CLIMATISEE"
                    chambres = ChambreClimatisee.objects.all()
                elif chambre.chambre_ventilee:
                    # Recuperer les chambres ventilées
                    chambrer = chambre.chambre_ventilee
                    typeChambre = "CHAMBRE VENTILEE"
                    chambres = ChambreVentilee.objects.all()

            # Passer les chambres en paramètres
            context = {
                'idChambre': chambre_id,
                'detailChambre': chambrer,
                'type': typeChambre,
                'chambres': chambres
            }

            # Afficher le template de la page d'acceuil
            return render(request, 'utilisateur/detailsChambre.html', context)

        else:
            return redirect('chambreDisponible')


# Detail de la chambre disponible avec vidéo
def detailChambreVideo(request, chambre_id):
    if 'emailUser' in request.session:

        if Chambre.objects.filter(id=chambre_id).exists():

            # Recuperer la chambre précise
            chamb = Chambre.objects.get(id=chambre_id)

            chambre = None

            if chamb:
                if chamb.suite:
                    # Recuperer la suite
                    chambre = chamb.suite
                elif chamb.chambre_climatisee:
                    # Recuperer la chambre climatisée
                    chambre = chamb.chambre_climatisee
                elif chamb.chambre_ventilee:
                    # Recuperer la chambre ventilée
                    chambre = chamb.chambre_ventilee

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

        if Chambre.objects.filter(id=chambre_id, statutChambre='libre').exists():

            # Recuperer la chambre précise
            chamb = Chambre.objects.get(id=chambre_id)

            chambre = None

            if chamb:
                if chamb.suite:
                    # Recuperer la suite
                    chambre = chamb.suite
                elif chamb.chambre_climatisee:
                    # Recuperer la chambre climatisée
                    chambre = chamb.chambre_climatisee
                elif chamb.chambre_ventilee:
                    # Recuperer la chambre ventilée
                    chambre = chamb.chambre_ventilee

            # Verifier que la requete est POST
            if request.method == 'POST':

                # Recuperer le formulaire de contact depuis la page
                form = ReservationChambreForm(request.POST)

                # Valider le formulaire de reservation
                if form.is_valid():
                    reservationChambre = form.save(commit=False)

                    reservationChambre.client = Utilisateur.objects.get(mail_utilisateur=request.session['emailUser'])

                    reservationChambre.chambre = Chambre.objects.get(id=chambre_id)

                    if form.cleaned_data['temps_sejour']:
                        reservationChambre.total_a_payer = int(chambre.prix_journee)*int(form.cleaned_data['temps_sejour'])
                    else:
                        reservationChambre.total_a_payer = int(chambre.prix_nuite)

                    reservationChambre.save()

                    sujet = "RESERVATION DE CHAMBRE"
                    message = (
                        f"Bonjour/Bonsoir, Vous serez contacter lors de la validation.")
                    envoyer_email(request.session['emailUser'], sujet, message)

                    # Recuperer vers le profil du client
                    return redirect('profil')

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


# Réservation de la chambre disponible
def reservationEvent(request):
    try:
        # Try to retrieve the Espace object
        espace = Espace.objects.get()  # Assume you are fetching the specific espace with id=1
    except Espace.DoesNotExist:
        espace = None  # If no Espace object exists, set espace to None

    # Check if the request method is POST
    if request.method == 'POST':
        # Get the reservation form from the page
        form = ReservationEventForm(request.POST)

        # Validate the reservation form
        if form.is_valid():
            reservationEspace = form.save(commit=False)
            reservationEspace.espace = espace
            # Fetch the client based on their email in the session
            reservationEspace.client = Utilisateur.objects.get(mail_utilisateur=request.session['emailUser'])
            reservationEspace.save()

            # Send an email confirmation
            sujet = "RESERVATION DE L'ESPACE"
            message = "Bonjour/Bonsoir, Vous serez contacter lors de la validation."
            envoyer_email(request.session['emailUser'], sujet, message)

            # Redirect to the profile page after successful reservation
            return redirect('profil')
    else:
        # If the request is not POST, instantiate an empty form
        form = ReservationEventForm()

    # Context data for rendering the template
    context = {
        'detailEspace': espace,
        'forms': form
    }

    # Render the reservationEvent.html template with the context data
    return render(request, 'utilisateur/reservationEvent.html', context)


# Pour l'optimisation SEO
def robots_txt(request):
    # Utiliser le BASE_URL de settings si défini, sinon fallback à request.get_host()
    base_url = settings.BASE_URL if hasattr(settings, 'BASE_URL') else f'http://{request.get_host()}'

    lines = [
        "User-Agent: *",
    ]
    if settings.DEBUG:
        # Bloquer tout accès aux robots en développement
        lines.extend([
            "Disallow: /admin/",
            "Disallow: /admini/",
            "Allow: /",
            f"Sitemap: https://espacekaribu.pythonanywhere.com/sitemap.xml",
        ])
    else:
        # En production, autoriser certaines sections et inclure le sitemap
        lines.extend([
            "Disallow: /admin/",
            "Disallow: /admini/",
            "Allow: /",
            f"Sitemap: {base_url}/sitemap.xml",
        ])

    return HttpResponse("\n".join(lines), content_type="text/plain")
