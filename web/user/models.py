from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(
        max_length=10, unique=True, blank=False, verbose_name="사용자 아이디"
    )
    user_name = models.CharField(max_length=20, blank=False, verbose_name="이름")
    password = models.CharField(max_length=15, blank=False, verbose_name="비밀번호")
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name="등록시간")

    def __str__(self):
        return self.user_id

    # db_table의 이름을 "tb_user로 설정"
    class Meta:
        db_table = "tb_user"


class Favorite(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="유저 PK")
    category = models.ForeignKey(
        "book.Category", on_delete=models.CASCADE, verbose_name="카테고리 PK"
    )

    def __str__(self):
        return self.user

    # db_table의 이름을 "tb_user로 설정"
    class Meta:
        db_table = "tb_userfavorite"


class Reading(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="유저 PK")
    book = models.ForeignKey(
    "book.Book",
    to_field="book_isbn",
    blank=False,
    on_delete=models.CASCADE,
    verbose_name="읽은 도서(PK)")
    
    def __str__(self):
        return self.user

    class Meta:
        db_table = "tb_reading" 


    
class Wish(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="유저 PK")
    book = models.ForeignKey(
    "book.Book",
    to_field="book_isbn",
    blank=False,
    on_delete=models.CASCADE,
    verbose_name="읽은 도서(PK)")
    
    def __str__(self):
        return self.user

    class Meta:
        db_table = "tb_wish" 