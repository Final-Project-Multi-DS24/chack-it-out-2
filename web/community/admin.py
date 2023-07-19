from django.contrib import admin
from .models import Community, Member


# Register your models here.
class CommunityAdmin(admin.ModelAdmin):
    list_display = ("id", "meeting_date", "meeting_place", "creator")


class MemberAdmin(admin.ModelAdmin):
    list_display = ("Communityid", "user_pk")


admin.site.register(Community, CommunityAdmin)
admin.site.register(Member, MemberAdmin)
