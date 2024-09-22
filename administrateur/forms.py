from django.contrib.auth.hashers import check_password
from django.core import validators
from django import forms
from utilisateur.models import ChambreClimatisee, ChambreVentilee, Suite, Espace, Administrateur


#code pour gerer le form de chambre climatisee
class AjoutChambreClim(forms.ModelForm):
    class Meta:
        #le modele pour la table dans la bd
        model = ChambreClimatisee
        #les champs de la table
        fields = ['numeroChambre','photo1','photo2','photo3','photo4','video1','video2','video3','description','prix_nuite','prix_journee','statutChambre']
        widgets = {
            
            'numeroChambre': forms.TextInput(attrs={'class': 'form-control'}),
            'photo1': forms.FileInput(attrs={'class': 'form-control'}),
            'photo2': forms.FileInput(attrs={'class': 'form-control'}),
            'photo3': forms.FileInput(attrs={'class': 'form-control'}),
            'photo4': forms.FileInput(attrs={'class': 'form-control'}),
            'video1': forms.FileInput(attrs={'class': 'form-control'}),
            'video2': forms.FileInput(attrs={'class': 'form-control'}),
            'video3': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'prix_nuite': forms.NumberInput(attrs={'class': 'form-control'}),
            'prix_journee': forms.NumberInput(attrs={'class': 'form-control'}),
            'statutChambre': forms.Select(attrs={'class': 'form-control'}),
             
            
        }


#code pour gerer le form de chambre ventilee
class AjoutChambreVent(forms.ModelForm):
    class Meta:
        #le modele pour la table dans la bd
        model = ChambreVentilee
        #les champs de la table
        fields = ['numeroChambre','photo1','photo2','photo3','photo4','video1','video2','video3','description','prix_nuite','prix_journee','statutChambre']
        widgets = {
            'numeroChambre': forms.TextInput(attrs={'class': 'form-control'}),
            'photo1': forms.FileInput(attrs={'class': 'form-control'}),
            'photo2': forms.FileInput(attrs={'class': 'form-control'}),
            'photo3': forms.FileInput(attrs={'class': 'form-control'}),
            'photo4': forms.FileInput(attrs={'class': 'form-control'}),
            'video1': forms.FileInput(attrs={'class': 'form-control'}),
            'video2': forms.FileInput(attrs={'class': 'form-control'}),
            'video3': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'prix_nuite': forms.NumberInput(attrs={'class': 'form-control'}),
            'prix_journee': forms.NumberInput(attrs={'class': 'form-control'}),
            'statutChambre': forms.Select(attrs={'class': 'form-control'}),
        }


#code pour gerer le form de suite
class AjoutSuite(forms.ModelForm):
    class Meta:
        #le modele pour la table dans la bd
        model = Suite
        #les champs de la table
        fields = ['numeroChambre','photo1','photo2','photo3','photo4','video1','video2','video3','description','prix_nuite','prix_journee','statutChambre']
        widgets = {
            'numeroChambre': forms.TextInput(attrs={'class': 'form-control'}),
            'photo1': forms.FileInput(attrs={'class': 'form-control'}),
            'photo2': forms.FileInput(attrs={'class': 'form-control'}),
            'photo3': forms.FileInput(attrs={'class': 'form-control'}),
            'photo4': forms.FileInput(attrs={'class': 'form-control'}),
            'video1': forms.FileInput(attrs={'class': 'form-control'}),
            'video2': forms.FileInput(attrs={'class': 'form-control'}),
            'video3': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'prix_nuite': forms.NumberInput(attrs={'class': 'form-control'}),
            'prix_journee': forms.NumberInput(attrs={'class': 'form-control'}),
            'statutChambre': forms.Select(attrs={'class': 'form-control'}),
        }


#code pour gerer le form de espace
class AjoutEspace(forms.ModelForm):
    class Meta:
        #le modele pour la table dans la bd
        model = Espace
        #les champs de la table
        fields = ['photo1','photo2','photo3','photo4','photo5','photo6','description','descriptionSalleReception','descriptionSalleVip','descriptionGarage','prix','statutEspace']
        widgets = {
            'photo1': forms.FileInput(attrs={'class': 'form-control'}),
            'photo2': forms.FileInput(attrs={'class': 'form-control'}),
            'photo3': forms.FileInput(attrs={'class': 'form-control'}),
            'photo4': forms.FileInput(attrs={'class': 'form-control'}),
            'photo5': forms.FileInput(attrs={'class': 'form-control'}),
            'photo6': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'descriptionSalleReception': forms.Textarea(attrs={'class': 'form-control'}),
            'descriptionSalleVip': forms.Textarea(attrs={'class': 'form-control'}),
            'descriptionGarage': forms.Textarea(attrs={'class': 'form-control'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control'}),
            'statutEspace': forms.Select(attrs={'class': 'form-control'}),
            
        }


class ConnexionForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'border w-full h-[70px]',
            'placeholder': 'E-mail',
            'id': 'email',
            'required': 'required'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'border w-full h-[70px]',
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
            user = Administrateur.objects.get(mail_utilisateur=email)  # Recherche de l'utilisateur par email
            if check_password(password, user.password):  # Vérifie si le mot de passe est correct
                return user
            else:
                return None
        except Administrateur.DoesNotExist:
            return None


class ConnexionCodeForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'border w-full h-[70px] md:w-[500px]',  # Classes CSS pour le style
                'placeholder': 'Entrez le code reçu ',
                'id': 'email',
                'required': 'required',
            }
        ),
        label="Code",
        max_length=6,  # Longueur maximale d'un code
        required=True,  # Le code est obligatoire
    )