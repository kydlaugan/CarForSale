from django.shortcuts import render , redirect 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import *
from django.urls import reverse
from django.core.files.base import ContentFile

# Create your views here.

def home(request):
    template_name = 'index.html'
    return render(request , template_name)


def liste(request):
    template_name = 'liste.html'
    voiture = Voiture.objects.all()
    return render(request , template_name , {'voiture':voiture })


def details(request , id):
    template_name = 'details.html'
    autres_voiture = Voiture.objects.exclude(id = id)
    voiture = Voiture.objects.get(id = id)
    fournisseur = Fournisseur.objects.get( id= voiture.fournisseur.id)
    return render(request , template_name , {'voiture':voiture , 'autres_voiture':autres_voiture , 'fournisseur':fournisseur})

@csrf_exempt
def creer_voiture(request , id  , *args, **kwargs):
    template_name = 'creation.html'
    f = Fournisseur.objects.get(id=id)
    if request.method == "POST":
        num_chassis = request.POST.get('num_chassis')
        marque = request.POST.get('marque')
        modele = request.POST.get('modele')
        carburant = request.POST.get('carburant')
        kilometrage = request.POST.get('kilometrage')
        puissance = request.POST.get('puissance')
        prix = request.POST.get('prix')
        description = request.POST.get('description')
        etat = request.POST.get('etat')
        img1 = request.FILES.get('img1')
        img2 = request.FILES.get('img2')
        img3 = request.FILES.get('img3')
        img4 = request.FILES.get('img4')
        new_v = Voiture.objects.create(fournisseur = f, num_chassis = num_chassis ,marque = marque ,modele = modele ,carburant = carburant ,kilometrage = kilometrage, puissance  = puissance , prix =  prix ,description = description ,etat = etat ,annee_validation='2023-02-23', img1=img1 , img2=img2 , img3=img3 , img4=img4)
        new_v.save()
    return render(request , template_name , {'f':f})

def dashboard(request , id):
    template_name = 'dash.html'
    # user_id = request
    fournisseur = Fournisseur.objects.get(id = id)
    # voiture = Voiture.objects.filter(fournisseur = user_id)
    voiture = Voiture.objects.filter(fournisseur = id)
    return render(request , template_name , {'voiture':voiture , 'fournisseur':fournisseur })

@csrf_exempt
def connexion(request , *args, **kwargs):
    template_name = 'connexion.html'
    nom = request.POST.get('nom')
    password = request.POST.get('password')
    client = Client.objects.filter(nom = nom ,password = password)
    fournisseur = Fournisseur.objects.filter(nom = nom ,password = password)
    c = Client.objects.filter(nom = nom ,password = password).count()
    for i in fournisseur :
        four = Fournisseur.objects.get(id = i.id)
    f =fournisseur.count()

    if f>0 :
        return redirect('dashboard/'+str(four.id) + '/')
    elif c>0:
        return redirect('home')
    return render(request , template_name)


@csrf_exempt
def register(request):
    template_name = 'register.html'
    if request.method == 'POST':
        fournisseur = Fournisseur()
        fournisseur.nom = request.POST['nom']
        fournisseur.adresse = request.POST['adresse']
        fournisseur.telephone = request.POST['telephone']
        fournisseur.email = request.POST['email']
        fournisseur.password = request.POST['password']
        fournisseur.save()
        return redirect('connexion')
    return render(request , template_name)


def delete_voiture(request ,id, *args , **kwargs):
    v = Voiture.objects.get(id = id)
    v.delete()
    return redirect(request.META['HTTP_REFERER'])



def a_jour_voiture(request ,id, *args , **kwargs):
    voiture = Voiture.objects.get(id = id)

    if request.method == "POST" :
            num_chassis = request.POST.get('num_chassis')
            marque = request.POST.get('marque')
            modele = request.POST.get('modele')
            carburant = request.POST.get('carburant')
            kilometrage = request.POST.get('kilometrage')
            puissance = request.POST.get('puissance')
            prix = request.POST.get('prix')
            description = request.POST.get('description')
            etat = request.POST.get('etat')
            img1 = request.FILES('img1')
            img2 = request.FILES.get('img2')
            img3 = request.FILES.get('img3')
            img4 = request.FILES.get('img4')

            voiture.num_chassis = num_chassis
            voiture.marque = marque
            voiture.modele = modele
            voiture.carburant = carburant
            voiture.kilometrage = kilometrage
            voiture.puissance = puissance
            voiture.prix = prix
            voiture.description = description
            voiture.etat = etat
            voiture.img1 = img1
            voiture.img2 = img2
            voiture.img3 = img3
            voiture.img4 = img4
            voiture.save()
    return render(request ,'modifier.html',{'v':voiture })

@csrf_exempt
def recherche(request , *args, **kwargs ):
    if request.method == "POST":
        marque = request.POST.get('marque')
        voiture = Voiture.objects.filter(marque = marque)
    return render(request , 'liste.html' , {'voiture':voiture})