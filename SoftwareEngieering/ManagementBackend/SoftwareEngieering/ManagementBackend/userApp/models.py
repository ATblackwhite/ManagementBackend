from django.db import models

class LibraryUser(models.Model):
    UserName = models.CharField(max_length=30,verbose_name='用户名')
    PassWord = models.CharField(max_length=30,verbose_name='密码')
    Name = models.CharField(max_length=30,verbose_name='姓名')
    Age = models.IntegerField(verbose_name='年龄')
    Gender_Choice = ((1, '男'), (2, '女'))
    Gender = models.IntegerField(choices=Gender_Choice,default=1,verbose_name='性别')
    Phone = models.CharField(max_length=30,verbose_name='电话')
    Email = models.CharField(max_length=30,verbose_name='邮箱')
    Comment = models.BooleanField(verbose_name='是否可评论')

    def __str__(self):
        return f'用户:{self.UserName}  评论权限:{self.Comment}'

    class Meta:
        verbose_name_plural='博物馆系统用户'


class KnowledgeUser(models.Model):
    UserName = models.CharField(max_length=30,verbose_name='用户名')
    PassWord = models.CharField(max_length=30,verbose_name='密码')
    Name = models.CharField(max_length=30,verbose_name='姓名')
    Age = models.IntegerField(verbose_name='年龄')
    Gender_Choice = ((1, '男'), (2, '女'))
    Gender = models.IntegerField(choices=Gender_Choice,default=1,verbose_name='性别')
    Phone = models.CharField(max_length=30,verbose_name='电话')
    Email = models.CharField(max_length=30,verbose_name='邮箱')
    Comment = models.BooleanField(verbose_name='是否可评论')

    def __str__(self):
        return f'用户:{self.UserName}  评论权限:{self.Comment}'

    class Meta:
        verbose_name_plural='知识服务系统用户'

