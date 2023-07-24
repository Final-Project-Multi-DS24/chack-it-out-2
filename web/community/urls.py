from django.urls import path
from .views import community, newcommunity,detail,quit

urlpatterns = [path("", community), 
              path("new/", newcommunity),
              path("detail/<str:pk>", detail),
              path("quit/<str:pk>",quit)            
              ]
