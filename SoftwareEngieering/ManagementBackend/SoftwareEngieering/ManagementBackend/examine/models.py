from django.db import models


class Comments(models.Model):
    """评论表"""
    user_id = models.IntegerField()
    literal_comment = models.CharField(verbose_name='用户的文字评论', max_length=200)
    date = models.DateTimeField(verbose_name='该条评论的时间', null=True)
    is_finished = models.BooleanField(verbose_name='该条评论是否审核过', default=False)
    image_comment = models.ImageField(verbose_name='用户的图片评论', null=True)


# Create your models here.

# class Users(models.Model):
#     user_name = models.CharField(verbose_name='用户名', max_length=20)
#     comment_permission = models.BooleanField(verbose_name='用户评论权限', default=False)
#     gender_tuple = ((1, "男"), (2, "女"))
#     gender = models.SmallIntegerField(verbose_name='性别', choices=gender_tuple)

# Create your models here.
