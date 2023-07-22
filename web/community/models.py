from django.db import models


# Create your models here.


class Community(models.Model):
    book = models.ForeignKey(
        "book.Book",
        blank=False,
        on_delete=models.CASCADE,
        verbose_name="도서",
    )
    meeting_date = models.DateTimeField(blank=False, verbose_name="모임 날짜")
    meeting_place = models.CharField(max_length=20, blank=False, verbose_name="모임 장소")
    creator= models.ForeignKey(
        "user.User",
        to_field="id",
        blank=False,
        on_delete=models.CASCADE,
        verbose_name="작성자",
    )
    is_finished = models.BooleanField(default=False)
    description = models.TextField()

    # db_table의 이름을 "tb_user로 설정"
    class Meta:
        db_table = "tb_community"


class Member(models.Model):
    community = models.ForeignKey("Community", on_delete=models.CASCADE)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)

    class Meta:
        db_table = "tb_communitymember"
