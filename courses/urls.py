from django.urls import path
from . import views

urlpatterns = [
    path('', views.kurslar),
    path('<int:course_id>/', views.kurs_detay), 
    path('<str:category_name>/', views.getCoursesByCategory),
]