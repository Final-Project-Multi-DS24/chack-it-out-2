from django.db import models


# Create your models here.
class Book(models.Model):
    book_isbn = models.IntegerField(unique=True, verbose_name="ISBN")
    book_title = models.CharField(max_length=500, verbose_name="도서명")
    book_author = models.CharField(max_length=20, verbose_name="저자")
    book_publisher = models.CharField(max_length=20, verbose_name="출판사")
    book_page = models.IntegerField(verbose_name="페이지 수")
    book_description = models.CharField(max_length=1000, verbose_name="책소개")
    book_cover = models.CharField(max_length=400, verbose_name="책표지")

    #
    def __str__(self):
        return self.book_title

    # db_table의 이름을 "tb_user로 설정"
    class Meta:
        db_table = "tb_book"
