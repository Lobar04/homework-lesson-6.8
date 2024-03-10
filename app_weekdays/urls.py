from django.urls import path
from django.http import HttpResponse
from .views import weekdays,weekdays_uz,weekdays_eng,weekdays_ru,main

urlpatterns = [
    path('weekdays/',weekdays,name='weekdays_url'),
    path('weekdays/uz/',weekdays_uz,name='weekdays_uz_url'),
    path('weekdays/en/',weekdays_eng,name='weekdays_en_url'),
    path('weekdays/ru/',weekdays_ru,name='weekdays_ru_url'),
    path('',main,name='main_url'),

]