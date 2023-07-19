from django.db import models


# Create your models here.


class Community(models.Model):
    book = models.ForeignKey(
        "book.Book",
        to_field="book_isbn",
        blank=False,
        on_delete=models.CASCADE,
        verbose_name="도서",
    )
    meeting_date = models.DateTimeField(blank=False, verbose_name="모임 날짜")
    meeting_place = models.CharField(max_length=20, blank=False, verbose_name="모임 장소")
    is_finished = models.BooleanField(default=False)
    description = models.TextField()

    # db_table의 이름을 "tb_user로 설정"
    class Meta:
        db_table = "tb_community"


class Member(models.Model):
    Communityid = models.ForeignKey("Community", on_delete=models.CASCADE)
    user_pk = models.ForeignKey("user.User", on_delete=models.CASCADE)
    is_leader = models.BooleanField(default=False)

    class Meta:
        db_table = "tb_communitymember"
