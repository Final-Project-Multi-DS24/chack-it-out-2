from django.urls import path
from .views import search,result

urlpatterns = [
    path('search/',search),
    path('search/result/',result)   
    ]
