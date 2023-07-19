from django.urls import path
from .views import community, newcommunity

urlpatterns = [path("", community), path("new/", newcommunity)]
