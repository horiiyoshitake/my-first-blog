from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):# オブジェクトを定義してますの宣言、POSTはモデルの名前。モデル名は大文字開始。
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE) #1:Nの関係を示すフィールド
    title = models.CharField(max_length=200) #文字列、メモリ管理上、最大値指定が必須
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title
