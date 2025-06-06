from django import forms
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password


from utilisateur.models import ContactAdmin, Utilisateur, CommandeLogement, CommandeEspace


# Etablir le formulaire de contact
class ContactForm(forms.Form):
    nom_complet = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'border w-full h-[70px] mt-3 mb-5 rounded',
            'placeholder': 'John Doe',
            'id': 'name',
            'required': 'required'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'border w-full h-[70px] mt-3 mb-5 rounded',
            'placeholder': 'example@gmail.com',
            'id': 'email',
            'required': 'required'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'border w-full h-[150px] mt-3 mb-5 rounded',
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
            mail=self.cleaned_data['email'],
            message=self.cleaned_data['message']
        )
        contact.save()


# Etablir le formulaire de connexion
class ConnexionForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'border w-full h-[70px] mt-2 mb-5 rounded text-black',
            'placeholder': 'E-mail',
            'id': 'email',
            'required': 'required'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border w-full h-[70px] mt-2 mb-5 rounded text-black',
            'placeholder': 'Mot de passe ',
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
                self.add_error(None,"E-mail ou mot de passe incorrect")

        return cleaned_data

    def authentifier_utilisateur(self, email, password):
        try:
            user = Utilisateur.objects.get(mail_utilisateur=email)  # Recherche de l'utilisateur par email
            if check_password(password, user.mot_de_passe):  # Vérifie si le mot de passe est correct
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
            'class': 'border w-full h-[70px] mt-2 mb-5 rounded text-black',
            'placeholder': 'Nom Complet',
            'id': 'name',
            'required': 'required'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'border w-full h-[70px] mt-2 mb-5 rounded text-black',
            'placeholder': 'E-mail',
            'id': 'email',
            'required': 'required'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border w-full h-[70px] mt-2 mb-5 rounded text-black',
            'placeholder': 'Mot de passe',
            'id': 'password',
            'required': 'required'
        })
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Utilisateur.objects.filter(mail_utilisateur=email).exists():
            self.add_error(None,"Cet e-mail est déjà utilisé.")
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
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'border w-full h-[70px] md:w-[500px] text-black px-2 rounded',  # Classes CSS pour le style
                'placeholder': 'Entrez votre E-mail',
                'id': 'email',
                'required': 'required',
            }
        ),
        label="Adresse e-mail",
        max_length=254,  # Longueur maximale d'un email
        required=True,  # L'email est obligatoire
    )


# Etablir le formulaire du mot de passe oublier Code
class PasseOublierCodeForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'border w-full h-[70px] md:w-[500px] px-2 rounded text-black',  # Classes CSS pour le style
                'placeholder': 'Entrez le code reçu ',
                'id': 'email',
                'required': 'required',
            }
        ),
        label="Code",
        max_length=6,  # Longueur maximale d'un code
        required=True,  # Le code est obligatoire
    )


# Etablir le formulaire pour changer le mot de passe
class ChangePasseForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border w-full h-[70px] md:w-[500px] px-2 rounded text-black',
            'placeholder': 'Nouveau mot de passe',
            'id': 'password',
            'required': 'required',
        }),
        label="Nouveau mot de passe",
        min_length=8,  # Vous pouvez spécifier une longueur minimale
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border w-full h-[70px] md:w-[500px] px-2 rounded text-black',
            'placeholder': 'Confirmer le mot de passe',
            'id': 'password2',
            'required': 'required',
        }),
        label="Confirmer le mot de passe",
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        # Vérifier si les deux mots de passe correspondent
        if password and password2 and password != password2:
            self.add_error(None,"Les mots de passe ne correspondent pas.")

        return cleaned_data


# Etablir le formulaire pour la reservation d'une chambre
class ReservationChambreForm(forms.ModelForm):
    class Meta:
        model = CommandeLogement
        fields = ['numero_contacter', 'date_arriver', 'heure_arriver', 'temps_sejour', 'choixSejour']

    # Personnaliser les widgets et leur apparence dans le formulaire
    numero_contacter = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'border w-full h-[70px] rounded my-3 px-2 rounded text-black',
            'placeholder': 'cel:1111112222',
            'required': 'required'
        })
    )
    date_arriver = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'my-3 rounded border mb-4 h-[50px]',
            'type': 'date',
            'required': 'required'
        })
    )
    heure_arriver = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'class': 'my-3 rounded border mb-4 h-[50px]',
            'type': 'time',
            'required': 'required'
        })
    )
    temps_sejour = forms.IntegerField(
        required=False,  # Initialement non requis
        widget=forms.NumberInput(attrs={
            'class': 'font-thin text-black border mb-4 h-[50px]',
            'placeholder': 'Nombre de jours',
            'required': 'required',
            'min': '0',  # Assurer que seuls les nombres positifs sont acceptés
            'id': 'temps_sejour_field',  # Attribuer un id pour le ciblage par JS
        })
    )
    choixSejour = forms.ChoiceField(
        choices=[('nuitée', 'Nuitée'), ('journée', 'Journée')],
        widget=forms.Select(attrs={
            'class': 'form-control my-3 border h-[50px]',
            'required': 'required',
            'id': 'choix_sejour_field',  # Attribuer un id pour le ciblage par JS
        })
    )


# Etablir le formulaire pour la reservation d'une chambre
class ReservationEventForm(forms.ModelForm):
    class Meta:
        model = CommandeEspace
        fields = ['numero_contacter', 'date_arriver']

    # Widgets personnalisés pour le rendu du formulaire
    numero_contacter = forms.CharField(
        label="Numéro à contacter",
        widget=forms.TextInput(attrs={
            'class': 'border w-full h-[70px] rounded my-3',
            'placeholder': 'cel:1111112222',
            'required': 'required'
        })
    )
    date_arriver = forms.DateField(
        label="Date d'arrivée",
        widget=forms.DateInput(attrs={
            'class': 'my-3 rounded',
            'type': 'date',
            'required': 'required'
        })
    )



class ModifNameForm(forms.Form):

    nom = forms.CharField(
        label='Nom',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'max-w-[600px] h-[50px] rounded my-3 px-10 text-black border border-gray-300 focus:border-blue-500  focus:outline-none focus:ring-2 focus:ring-blue-500',
            'id': 'name',
            'placeholder': 'Entrer votre nom'
        }),
        required=True
    )




class ModifPasseForm(forms.Form):

    current_password = forms.CharField(
        label='Mot de passe actuel',
        widget=forms.PasswordInput(attrs={
            'class': 'max-w-[600px] h-[50px] rounded my-3 px-10 text-black border border-gray-300 focus:border-blue-500  focus:outline-none focus:ring-2 focus:ring-blue-500',
            'id': 'password',
            'placeholder': 'Entrer votre mot de passe actuel'
        }),
        required=False
    )

    new_password = forms.CharField(
        label='Nouveau mot de passe',
        widget=forms.PasswordInput(attrs={
            'class': 'max-w-[600px] h-[50px] rounded my-3 px-10 text-black border border-gray-300 focus:border-blue-500  focus:outline-none focus:ring-2 focus:ring-blue-500',
            'id': 'newpassword',
            'placeholder': 'Entrer un nouveau mot de passe'
        }),
        required=False
    )

    confirm_password = forms.CharField(
        label='Confirmez le mot de passe',
        widget=forms.PasswordInput(attrs={
            'class': 'max-w-[600px] h-[50px] rounded my-3 px-10 text-black border border-gray-300 focus:border-blue-500  focus:outline-none focus:ring-2 focus:ring-blue-500',
            'id': 'confirmpassword',
            'placeholder': 'Confirmer le nouveau mot de passe'
        }),
        required=False
    )


    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ModifPasseForm, self).__init__(*args, **kwargs)



    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data.get('current_password')
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        # Check if the old password matches
        if not check_password(current_password, self.user.mot_de_passe):
            self.add_error(None, "L'ancien mot de passe est incorrect.")

        # Check if the new passwords match
        if new_password != confirm_password:
            self.add_error(None, "Les mots de passe ne correspondent pas.")

