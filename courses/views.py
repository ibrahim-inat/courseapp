from django.http import HttpResponse
from django.shortcuts import render


# http://127.0.0.1:8000/client => anasayfa
# http://127.0.0.1:8000/client/home => anasayfa
# http://127.0.0.1:8000/client/kurslar => kurs listesi

def home (request):
    return HttpResponse('anasayfa')
def kurslar (request):
    return HttpResponse('kurslar')