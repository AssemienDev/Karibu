from django.db import models


# Modèle pour l'espace
class Espace(models.Model):
    photo1 = models.ImageField(upload_to='document/espaces/', blank=True, null=True)
    photo2 = models.ImageField(upload_to='document/espaces/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='document/espaces/', blank=True, null=True)
    photo4 = models.ImageField(upload_to='document/espaces/', blank=True, null=True)
    photo5 = models.ImageField(upload_to='document/espaces/', blank=True, null=True)
    photo6 = models.ImageField(upload_to='document/espaces/', blank=True, null=True)
    description = models.TextField(blank=False, null=False)
    descriptionSalleReception = models.TextField(blank=True, null=True)
    descriptionSalleVip = models.TextField(blank=True, null=True)
    descriptionGarage = models.TextField(blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

# Modèle pour les suites
class Suite(models.Model):
    numeroChambre = models.CharField(max_length=10, blank=True, null=True)
    photo1 = models.ImageField(upload_to='document/suites/images/', blank=True, null=True)
    photo2 = models.ImageField(upload_to='document/suites/images/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='document/suites/images/', blank=True, null=True)
    photo4 = models.ImageField(upload_to='document/suites/images/', blank=True, null=True)
    video1 = models.FileField(upload_to='document/suites/videos/', blank=True, null=True)
    video2 = models.FileField(upload_to='document/suites/videos/', blank=True, null=True)
    video3 = models.FileField(upload_to='document/suites/videos/', blank=True, null=True)
    description = models.TextField()
    prix_nuite = models.DecimalField(max_digits=10, decimal_places=2)
    prix_journee = models.DecimalField(max_digits=10, decimal_places=2)
    statutChambre = models.CharField(max_length=20, null=True, blank=True)
    STATUT_CHOICES = [
        ('libre', 'Libre'),
        ('occupe', 'Occupé'),
    ]

    
    statutChambre = models.CharField(max_length=10, choices=STATUT_CHOICES, default='libre')

# Modèle pour les chambres climatisées
class ChambreClimatisee(models.Model):
    numeroChambre = models.CharField(max_length=10, blank=True, null=True)
    photo1 = models.ImageField(upload_to='document/chambres_climatisees/images/', blank=True, null=True)
    photo2 = models.ImageField(upload_to='document/chambres_climatisees/images/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='document/chambres_climatisees/images/', blank=True, null=True)
    photo4 = models.ImageField(upload_to='document/chambres_climatisees/images/', blank=True, null=True)
    video1 = models.FileField(upload_to='document/chambres_climatisees/videos/', blank=True, null=True)
    video2 = models.FileField(upload_to='document/chambres_climatisees/videos/', blank=True, null=True)
    video3 = models.FileField(upload_to='document/chambres_climatisees/videos/', blank=True, null=True)
    description = models.TextField()
    prix_nuite = models.DecimalField(max_digits=10, decimal_places=2)
    prix_journee = models.DecimalField(max_digits=10, decimal_places=2)
    STATUT_CHOICES = [
        ('libre', 'Libre'),
        ('occupe', 'Occupé'),
    ]

  
    statutChambre = models.CharField(max_length=10, choices=STATUT_CHOICES, default='libre')

# Modèle pour les chambres ventilées
class ChambreVentilee(models.Model):
    numeroChambre = models.CharField(max_length=10, blank=True, null=True)
    photo1 = models.ImageField(upload_to='document/chambres_ventilees/images/', blank=True, null=True)
    photo2 = models.ImageField(upload_to='document/chambres_ventilees/images/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='document/chambres_ventilees/images/', blank=True, null=True)
    photo4 = models.ImageField(upload_to='document/chambres_ventilees/images/', blank=True, null=True)
    video1 = models.FileField(upload_to='document/chambres_ventilees/videos/', blank=True, null=True)
    video2 = models.FileField(upload_to='document/chambres_ventilees/videos/', blank=True, null=True)
    video3 = models.FileField(upload_to='document/chambres_ventilees/videos/', blank=True, null=True)
    description = models.TextField()
    prix_nuite = models.DecimalField(max_digits=10, decimal_places=2)
    prix_journee = models.DecimalField(max_digits=10, decimal_places=2)
    statutChambre = models.CharField(max_length=20, null=True, blank=True)
    STATUT_CHOICES = [
        ('libre', 'Libre'),
        ('occupe', 'Occupé'),
    ]

    
    statutChambre = models.CharField(max_length=10, choices=STATUT_CHOICES, default='libre')


# Modèle pour les utilisateurs
class Utilisateur(models.Model):
    nom_complet = models.CharField(max_length=255)
    mail_utilisateur = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=128)


# Modèle pour les commandes d'espace
class CommandeEspace(models.Model):
    numero_contacter = models.CharField(max_length=20)
    date_arriver = models.DateField()
    espace = models.ForeignKey(Espace, on_delete=models.CASCADE)
    client = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True, blank=True)


class CommandeLogement(models.Model):
    numero_contacter = models.CharField(max_length=20)
    date_arriver = models.DateField()
    heure_arriver = models.TimeField()
    temps_sejour = models.IntegerField()  # Durée du séjour en jours
    chambre = models.ForeignKey('Chambre', on_delete=models.CASCADE)
    choixSejour = models.CharField(max_length=20, null=True, blank=True)
    total_a_payer = models.CharField(max_length=50)
    client = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True, blank=True)


# Modèle pour les chambres
class Chambre(models.Model):
    chambre_climatisee = models.OneToOneField(ChambreClimatisee, on_delete=models.CASCADE, null=True, blank=True)
    chambre_ventilee = models.OneToOneField(ChambreVentilee, on_delete=models.CASCADE, null=True, blank=True)
    suite = models.OneToOneField(Suite, on_delete=models.CASCADE, null=True, blank=True)
    statutChambre = models.CharField(max_length=20,null=True, blank=True)


# Modèle pour les administrateurs
class Administrateur(models.Model):
    nom = models.CharField(max_length=255)
    mail_admin = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=128)


# Modèle pour le formulaire de contact
class ContactAdmin(models.Model):
    nom_complet = models.CharField(max_length=255)
    mail = models.EmailField(unique=True)
    message = models.TextField()


# Modèle pour le code de récupération
class CodeRecuperationUser(models.Model):
    client = models.ForeignKey('Utilisateur', on_delete=models.CASCADE, blank=True, null=True)
    code = models.CharField(max_length=6)


# Modèle pour le code de connexion de l'administrateur
class CodeConnexionAdmin(models.Model):
    admin = models.ForeignKey('Administrateur', on_delete=models.CASCADE, blank=True, null=True)
    code = models.CharField(max_length=6)

