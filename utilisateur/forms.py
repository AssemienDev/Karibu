from django.forms import forms


# Etablir le formulaire de contact
class ContactForm(forms.Form):
    pass


# Etablir le formulaire de connexion
class ConnexionForm(forms.Form):
    pass


# Etablir le formulaire d'inscription
class InscriptionForm(forms.Form):
    pass


# Etablir le formulaire du mot de passe oublier Email
class PasseOublierEmailForm(forms.Form):
    pass


# Etablir le formulaire du mot de passe oublier Code
class PasseOublierCodeForm(forms.Form):
    pass


# Etablir le formulaire pour changer le mot de passe
class ChangePasseForm(forms.Form):
    pass


# Etablir le formulaire pour la reservation d'une chambre
class ReservationChambreForm(forms.Form):
    pass


# Etablir le formulaire pour la reservation payements d'une chambre
class ReservationChambrePayementsForm(forms.Form):
    pass