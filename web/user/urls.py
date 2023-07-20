from django.urls import path
# from .views import view의 함수명 
from .views import register,login,logout,userpage,search,delete,reading,wish,usercommunity

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('logout/', logout),
    path('userpage/',userpage),
    path('search/',search),
    path('delete/',delete),
    path('userpage/reading',reading),
    path('userpage/wish',wish),
    path('userpage/usercommunity',usercommunity)
]