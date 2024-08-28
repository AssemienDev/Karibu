from django.db import models

# Modèle pour l'espace
class Espace(models.Model):
    photo1 = models.ImageField(upload_to='document/espaces/', blank=False, null=False)
    photo2 = models.ImageField(upload_to='document/espaces/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='document/espaces/', blank=True, null=True)
    photo4 = models.ImageField(upload_to='document/espaces/', blank=True, null=True)
    photo5 = models.ImageField(upload_to='document/espaces/', blank=True, null=True)
    photo6 = models.ImageField(upload_to='document/espaces/', blank=True, null=True)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)

# Modèle pour les suites
class Suite(models.Model):
    photo1 = models.ImageField(upload_to='document/suites/', blank=False, null=False)
    photo2 = models.ImageField(upload_to='document/suites/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='document/suites/', blank=True, null=True)
    photo4 = models.ImageField(upload_to='document/suites/', blank=True, null=True)
    description = models.TextField()
    prix_nuite = models.DecimalField(max_digits=10, decimal_places=2)
    prix_journee = models.DecimalField(max_digits=10, decimal_places=2)

# Modèle pour les chambres climatisées
class ChambreClimatisee(models.Model):
    photo1 = models.ImageField(upload_to='document/chambres_climatisees/', blank=False, null=False)
    photo2 = models.ImageField(upload_to='document/chambres_climatisees/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='document/chambres_climatisees/', blank=True, null=True)
    photo4 = models.ImageField(upload_to='document/chambres_climatisees/', blank=True, null=True)
    description = models.TextField()
    prix_nuite = models.DecimalField(max_digits=10, decimal_places=2)
    prix_journee = models.DecimalField(max_digits=10, decimal_places=2)

# Modèle pour les chambres ventilées
class ChambreVentilee(models.Model):
    photo1 = models.ImageField(upload_to='document/chambres_ventilees/', blank=False, null=False)
    photo2 = models.ImageField(upload_to='document/chambres_ventilees/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='document/chambres_ventilees/', blank=True, null=True)
    photo4 = models.ImageField(upload_to='document/chambres_ventilees/', blank=True, null=True)
    description = models.TextField()
    prix_nuite = models.DecimalField(max_digits=10, decimal_places=2)
    prix_journee = models.DecimalField(max_digits=10, decimal_places=2)

# Modèle pour les commandes d'espace
class CommandeEspace(models.Model):
    numero_contacter = models.CharField(max_length=20)
    date_arriver = models.DateField()
    espace = models.ForeignKey(Espace, on_delete=models.CASCADE)

# Modèle pour les commandes de logement
class CommandeLogement(models.Model):
    numero_contacter = models.CharField(max_length=20)
    date_arriver = models.DateField()
    heure_arriver = models.TimeField()
    temps_sejour = models.IntegerField()  # Durée du séjour en heures ou jours
    chambre = models.ForeignKey('Chambre', on_delete=models.CASCADE)

# Modèle pour les chambres
class Chambre(models.Model):
    chambre_climatisee = models.OneToOneField(ChambreClimatisee, on_delete=models.CASCADE, null=True, blank=True)
    chambre_ventilee = models.OneToOneField(ChambreVentilee, on_delete=models.CASCADE, null=True, blank=True)
    suite = models.OneToOneField(Suite, on_delete=models.CASCADE, null=True, blank=True)

# Modèle pour les paiements
class Paiement(models.Model):
    num_depot = models.CharField(max_length=20)
    capture_depot = models.ImageField(upload_to='document/paiements/')

# Modèle pour les utilisateurs
class Utilisateur(models.Model):
    nom_complet = models.CharField(max_length=255)
    mail_admin = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=128)

# Modèle pour les administrateurs
class Administrateur(models.Model):
    nom = models.CharField(max_length=255)
    mail_admin = models.EmailField(unique=True)
    mot_de_passe = models.CharField(max_length=128)
