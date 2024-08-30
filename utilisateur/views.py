from django.contrib.messages.storage import session
from django.shortcuts import render, redirect

from utilisateur.forms import ContactForm, ConnexionForm, InscriptionForm, PasseOublierEmailForm, PasseOublierCodeForm
from utilisateur.models import Chambre


# La Vue de l'acceuil
def index(request):
    # Recuperer les chambres
    chambre = Chambre.objects.filter(statutChambre='LIBRE')[:6]

    # Passer les chambres en paramètres
    context = {
        'chambre': chambre
    }

    # Afficher le template de la page d'acceuil
    return render(request,'index.html',context)


# La Vue du contact
def contact(request):
    # Verifier que la requete est POST
    if request.method == 'POST':

        # Recuperer le formulaire de contact depuis la page
        form = ContactForm(request.POST)

        # Valider le formulaire de contact
        if form.is_valid():

            # Recuperer vers la page d'Acceuil
            return redirect('acceuil')

    # Recuperer le formulaire de contact
    form = ContactForm()

    # Passer le form de contact en paramètres
    context = {
        'formContact': form
    }

    # Afficher le template de la page de contact
    return render(request,'contact.html',context)


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
                # session['emailUser'] = form.cleaned_data['emailUser']
                # Recuperer vers la page d'Acceuil
                return redirect('acceuil')

        # Recuperer le formulaire de connexion
        form = ConnexionForm()

        # Passer le form de contact en paramètres
        context = {
            'formConnexion': form
        }

        # Afficher le template de la page de connexion
        return render(request, 'connexion.html', context)


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
                # Recuperer vers la page d'Acceuil
                return redirect('connexion')

        # Recuperer le formulaire d'inscription
        form = InscriptionForm()

        # Passer le form de contact en paramètres
        context = {
            'formInscription': form
        }

        # Afficher le template de la page d'inscription
        return render(request, 'inscription.html', context)


# La Vue du passe oublié Email
def passeOublierEmail(request):
    if 'emailUser' in request.session:
        return redirect('acceuil')
    else:
        # Verifier que la requete est POST
        if request.method == 'POST':

            # Recuperer le formulaire de contact depuis la page
            form = PasseOublierEmailForm(request.POST)

            # Valider le formulaire de contact
            if form.is_valid():
                # Recuperer vers la page d'Acceuil
                return redirect('acceuil')

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
            form = PasseOublierCodeForm(request.POST)

            # Valider le formulaire de contact
            if form.is_valid():
                # Recuperer vers la page d'Acceuil
                return redirect('acceuil')

        # Recuperer le formulaire du code lors du mot de passe oublier
        form = PasseOublierCodeForm()

        # Passer le form de contact en paramètres
        context = {
            'formCode': form
        }

        # Afficher le template de la page de code
        return render(request, 'passeOublierCode.html', context)


# La Vue du message
def passeOublierMessage(request):
    if 'emailUser' in request.session:
        return redirect('acceuil')
    else:
        # Afficher le template de la page de message
        return render(request,'passeOublierMessage.html')


# La Vue des chambres disponibles
def listeChambreDisponible(request):
    # Recuperer les chambres
    chambre = Chambre.objects.filter(statutChambre='LIBRE')

    # Passer les chambres en paramètres
    context = {
        'chambre': chambre
    }

    # Afficher le template de la page d'acceuil
    return render(request, 'chambresDisponible.html', context)