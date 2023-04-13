from django.db import models

# Create your models here.

class Genre(models.Model):
    nom = models.CharField(max_length=250)

class Editeur(models.Model):
    nom = models.CharField(max_length=250)

class Auteur(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)

class Livre(models.Model):
    titre = models.CharField(max_length=250)
    description = models.TextField(max_length=2048, default=None)
    isbn = models.CharField(max_length=250, default=None)
    archive = models.BooleanField(default=None)
    editeur = models.ForeignKey(Editeur, on_delete=models.CASCADE, default=None)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE, default=None)
    genres = models.ManyToManyField(Genre, default=None)

class Stock(models.Model):
    emplacement = models.CharField(max_length=250)

class Usure(models.Model):
    nom = models.CharField(max_length=250)

class Exemplaire(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, default=None)
    usure = models.ForeignKey(Usure, on_delete=models.CASCADE, default=None)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, default=None)

class Adherent(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    telephone = models.CharField(max_length=250)
    email = models.EmailField
    caution = models.BooleanField

class emprunt(models.Model):
    exemplaire = models.ForeignKey(Exemplaire, on_delete=models.CASCADE, default=None)
    adherent = models.ForeignKey(Adherent, on_delete=models.CASCADE, default=None)
    date_emprunt = models.DateField
    date_retour = models.DateField
    status = models.CharField(max_length=250)

