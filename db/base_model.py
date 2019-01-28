from django.db import models

#定义model的基本类,共有的东西提取出来
class BaseModel(models.Model):
    '模块抽象基类'
    creat_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True,verbose_name="更新时间")
    is_delete = models.BooleanField(default=False,verbose_name="删除标记")


    class Meta:
        #说明是一个抽象模型类
        abstract = True