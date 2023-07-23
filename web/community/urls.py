from django.urls import path
from .views import community, newcommunity,detail

urlpatterns = [path("", community), 
              path("new/", newcommunity),
              path("detail/<str:pk>", detail)            
              ]
