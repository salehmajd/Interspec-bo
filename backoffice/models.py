import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Genre(models.Model):
    nom = models.CharField(max_length=250)
    def __str__(self):
        return self.nom

class Editeur(models.Model):
    nom = models.CharField(max_length=250)
    def __str__(self):
        return self.nom

class Auteur(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    def __str__(self):
        return self.nom + " " + self.prenom

class Livre(models.Model):
    titre = models.CharField(max_length=250)
    description = models.TextField(max_length=2048, default=None)
    isbn = models.CharField(max_length=250, default=None)
    archive = models.BooleanField(default=None)
    editeur = models.ForeignKey(Editeur, on_delete=models.CASCADE, default=None)
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE, default=None)
    genres = models.ManyToManyField(Genre, default=None)
    def __str__(self):
        return self.titre

class Stock(models.Model):
    emplacement = models.CharField(max_length=250)
    def __str__(self):
        return self.emplacement

class Usure(models.Model):
    nom = models.CharField(max_length=250)
    def __str__(self):
        return self.nom

class Exemplaire(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, default=None)
    usure = models.ForeignKey(Usure, on_delete=models.CASCADE, default=None)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.livre

class Adherent(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    telephone = models.CharField(max_length=250)
    email = models.EmailField
    caution = models.BooleanField
    def __str__(self):
        return self.nom + " " + self.prenom

class emprunt(models.Model):
    exemplaire = models.ForeignKey(Exemplaire, on_delete=models.CASCADE, default=None)
    adherent = models.ForeignKey(Adherent, on_delete=models.CASCADE, default=None)
    date_emprunt = models.DateTimeField("date emprunt")
    date_retour = models.DateTimeField("date retour")
    status = models.CharField(max_length=250)
    def __str__(self):
        return self.date_emprunt
    def emprunte_recemment(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_emprunt <= now

    def en_retard(self):
        now = timezone.now()
        return self.date_retour <= now

