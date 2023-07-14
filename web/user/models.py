from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.CharField(max_length=10, unique=True, blank=False, verbose_name='사용자 아이디')
    user_name=models.CharField(max_length=10, blank=False,verbose_name='이름')
    password=models.CharField(max_length=15, blank=False,verbose_name='비밀번호')
    profile_image=models.ImageField(upload_to='profile_images/', blank=True)
    registered_dttm=models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    # interest_list=models.ManyToManyField("book app의 book모델의"category)
    
    #  
    def __str__(self):
        return self.user_id
    # db_table의 이름을 "tb_user로 설정"
    class Meta:
        db_table = 'tb_user'