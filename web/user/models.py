from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.CharField(max_length=10, unique=True, verbose_name='사용자 아이디')
    user_name=models.CharField(max_length=10, verbose_name='이름')
    password=models.CharField(max_length=15, verbose_name='비밀번호')
    user_birth=models.DateField(verbose_name='생년월일', blank=True)
    phonenumber=models.CharField(max_length=15, verbose_name='전화번호', blank=True)
    profile_image=models.ImageField(upload_to='profile_images/', blank=True)
    registered_dttm=models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    # interest_list=models.ManyToManyField("book app의 book모델의"category)

    def __str__(self):
        return self.user_id
    class Meta:
        db_table = 'tb_user'