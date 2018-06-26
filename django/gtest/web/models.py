from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Testcase(models.Model):
    git_url     = models.CharField(max_length=30, verbose_name='Git地址')
    commit_id   = models.CharField(max_length=30, default="latest", verbose_name='Commit ID')
    user_name   = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="用户")
    test_case   = models.FileField(upload_to='./upload', verbose_name='测试用例')#文件名
    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')
    last_use    = models.DateTimeField(auto_now=True, verbose_name='最后一次执行')
    use_count   = models.IntegerField(default=0, verbose_name='执行次数')

    def __str__(self):
        return self.git_url

    class Meta:
        verbose_name_plural = verbose_name = u'测试用例'
        ordering=['last_use']#排序风格

