import requests 
from .models import CatFact
from django.http import HttpResponse
from django.db import IntegrityError

def get_cat_fact(request):
    response = requests.get('https://catfact.ninja/fact').json()
    fact = response['fact']
    try:
        CatFact(fact=fact).save()
        return HttpResponse('added new fact')
    except IntegrityError:
        # ok
        return HttpResponse('duplicate fact, ignoring')

