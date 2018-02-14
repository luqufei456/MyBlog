from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    atitle = models.CharField(max_length=50)
    alabel = models.CharField(max_length=20, blank=True) #允许为空白
    adate_time = models.DateTimeField(auto_now_add=True)#当对象第一次被创建时自动设置当前时间，用于创建的时间戳
    acontent = models.TextField(blank=True, null=True) #默认显示 可以为空

    # 获取URL并转换成url的表示格式
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id}) # 这里reverse 动态链接的第一个参数是url配置里的name 然后就会根据urls里的配置动态生成链接
        return "https://127.0.0.1:8000%s" % path

    def __str__(self):
        return self.atitle

    class Meta:
        ordering = ['-adate_time']  #元选项 按时间降序排列   排序会增加数据库的开销