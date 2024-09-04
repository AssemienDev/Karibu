from django import forms
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password


from utilisateur.models import ContactAdmin, Utilisateur


# Etablir le formulaire de contact
class ContactForm(forms.Form):
    nom_complet = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full h-[70px] mt-3 mb-5 rounded',
            'placeholder': 'John Doe',
            'id': 'name',
            'required': 'required'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full h-[70px] mt-3 mb-5 rounded',
            'placeholder': 'example@gmail.com',
            'id': 'email',
            'required': 'required'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'w-full h-[150px] mt-3 mb-5 rounded',
            'placeholder': 'Ici votre message ...',
            'id': 'message',
            'rows': 10,
            'required': 'required'
        })
    )

    class Meta:
        model = ContactAdmin
        fields = ['nom_complet', 'email', 'message']

    def save(self):
        # Création de l'objet ContactAdmin à partir des données du formulaire
        contact = ContactAdmin(
            nom_complet=self.cleaned_data['nom_complet'],
            email=self.cleaned_data['email'],
            message=self.cleaned_data['message']
        )
        contact.save()


# Etablir le formulaire de connexion
class ConnexionForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full h-[70px]',
            'placeholder': 'E-mail',
            'id': 'email',
            'required': 'required'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full h-[70px]',
            'placeholder': 'Mot de passe',
            'id': 'password',
            'required': 'required'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = self.authentifier_utilisateur(email, password)
            if not user:
                raise self.add_error(self,"E-mail ou mot de passe incorrect")

        return cleaned_data

    def authentifier_utilisateur(self, email, password):
        try:
            user = Utilisateur.objects.get(mail_utilisateur=email)  # Recherche de l'utilisateur par email
            if check_password(password, user.password):  # Vérifie si le mot de passe est correct
                return user
            else:
                return None
        except Utilisateur.DoesNotExist:
            return None


# Etablir le formulaire d'inscription
class InscriptionForm(forms.Form):

    nom_complet = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full h-[70px]',
            'placeholder': 'Nom Complet',
            'id': 'name',
            'required': 'required'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full h-[70px]',
            'placeholder': 'E-mail',
            'id': 'email',
            'required': 'required'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full h-[70px]',
            'placeholder': 'Mot de passe',
            'id': 'password',
            'required': 'required'
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Utilisateur.objects.filter(mail_utilisateur=email).exists():
            raise self.add_error(self,"Cet e-mail est déjà utilisé.")
        return email

    def save(self):
        data = self.cleaned_data
        new_user = Utilisateur(
            nom_complet=data['nom_complet'],
            mail_utilisateur=data['email'],
            mot_de_passe=make_password(data['password'])  # Hash le mot de passe
        )
        new_user.save()
        return new_user


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

