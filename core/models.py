from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# Create your models here.


class Client(models.Model):
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    adresse = models.CharField(max_length=20)
    telephone = models.IntegerField()
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    class Meta:
       verbose_name = "Client"
       verbose_name_plural = "Clients"


class Fournisseur (models.Model):
    nom = models.CharField(max_length=30)
    adresse = models.CharField(max_length=30)
    telephone = models.IntegerField()
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

class Voiture(models.Model):
    fournisseur = models.ForeignKey(Fournisseur , on_delete=models.CASCADE)
    num_chassis = models.IntegerField()
    marque = models.CharField(max_length=20)
    modele = models.CharField(max_length=30)
    annee_validation = models.DateField()
    kilometrage = models.CharField(max_length=30)
    puissance = models.CharField(max_length=30)
    prix = models.IntegerField()
    carburant = models.CharField(max_length=10)
    description = models.CharField(max_length=400 , blank=True)
    etat = models.CharField(max_length=10)
    etat = models.IntegerField()
    img1 = models.ImageField(upload_to='profile',blank=True)
    img2 = models.ImageField(upload_to='profile',blank=True)
    img3 = models.ImageField(upload_to='profile',blank=True)
    img4 = models.ImageField(upload_to='profile',blank=True)
    img5 = models.ImageField(upload_to='profile',blank=True)

    class Meta:
       verbose_name = "Voiture"
       verbose_name_plural = "Voitures"


class Annonce(models.Model):
    voiture = models.ForeignKey(Voiture , on_delete=models.CASCADE)
    date_creation = models.DateField()
    description_annonce = models.CharField(max_length=400)
    class Meta:
       verbose_name = "Annonce"
       verbose_name_plural = "Annonces"


# class Image(models.Model):
#     voiture = models.ForeignKey(Voiture , on_delete=models.CASCADE)
#     face = models.ImageField(upload_to='profile',blank=True)
#     voiture = models.ForeignKey(Voiture , on_delete=models.CASCADE)
#     arriere = models.ImageField(upload_to='profile',blank=True)
#     haut = models.ImageField(upload_to='profile',blank=True)
#     bas = models.ImageField(upload_to='profile',blank=True)
#     interieur = models.ImageField(upload_to='profile',blank=True)
#     class Meta:
#        verbose_name = "Image"
#        verbose_name_plural = "Images"




