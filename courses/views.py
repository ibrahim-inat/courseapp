from django.shortcuts import render
from django.http import HttpResponse 
from .models import Course

# 1. Kurs listesini (Veritabanından) getiren fonksiyon
from .models import Course, Category # Category modelini de eklediğinden emin ol

def kurslar(request):
    kurs_listesi = Course.objects.filter(isActive=True)
    kategoriler = Category.objects.all() # Tüm kategorileri veri tabanından çek
    
    return render(request, 'kurslar.html', {
        'kurslar': kurs_listesi,
        'kategoriler': kategoriler # Kategorileri HTML'e gönder
    })

# 2. Kategorileri yakalayan fonksiyon (Hata veren yer burasıydı, eksik olduğu için)
def getCoursesByCategory(request, category_name):
    # 1. Seçilen kategoriye ait aktif kursları getir
    kurslar = Course.objects.filter(category__slug=category_name, isActive=True)
    
    # 2. Sol taraftaki menü (sidebar) kaybolmasın diye tüm kategorileri tekrar çek
    kategoriler = Category.objects.all()
    
    return render(request, 'kurslar.html', {
        'kurslar': kurslar,
        'kategoriler': kategoriler
    })

def kurs_detay(request, course_id):
    # Veritabanından ID'si gelen sayıya eşit olan İLK kursu bul:
    kurs = Course.objects.get(pk=course_id) 
    
    return render(request, 'detay.html', {
        'kurs': kurs
    })