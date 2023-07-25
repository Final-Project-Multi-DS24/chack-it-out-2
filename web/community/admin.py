from django.contrib import admin
from .models import Community, Member, reviewMember,meetingbookscore


# Register your models here.
class CommunityAdmin(admin.ModelAdmin):
    list_display = ("id", "meeting_date", "meeting_place", "creator")


class MemberAdmin(admin.ModelAdmin):
    list_display = ("id", "user")

class reviewMemberAdmin(admin.ModelAdmin):
    list_display = ("community", "review")

class meetingbookscoreAdmin(admin.ModelAdmin):
    list_display = ("community", "score")

admin.site.register(Community, CommunityAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(reviewMember, reviewMemberAdmin)
admin.site.register(meetingbookscore, meetingbookscoreAdmin)

