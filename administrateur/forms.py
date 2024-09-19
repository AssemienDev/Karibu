from django.core import validators
from django import forms
from utilisateur.models import ChambreClimatisee,ChambreVentilee,Suite,Espace

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
        fields = ['photo1','photo2','photo3','photo4','photo5','photo6','description','descriptionSalleReception','descriptionSalleVip','descriptionGarage','prix']
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
            
        }