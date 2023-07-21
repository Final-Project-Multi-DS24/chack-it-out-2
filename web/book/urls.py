from django.urls import path
from .views import search, result, result2

urlpatterns = [
    path("search/", search),
    path("search/result/<str:pk>/", result),
    path("search/result2/<str:pk>/", result2),
]
