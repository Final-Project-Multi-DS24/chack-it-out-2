from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=('user_id','user_name','registered_dttm')
class FavoriteAdmin(admin.ModelAdmin):
    list_display=('user','category')


# User 앱 관리자에서 보여주기
admin.site.register(User, UserAdmin)