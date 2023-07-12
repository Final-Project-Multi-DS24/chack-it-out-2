from django.urls import path
# from .views import view의 함수명 
from .views import register, login,logout,userpage,modify,search

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    path('userpage/',userpage),
    path('modify/',modify),
    path('search/',search)
]