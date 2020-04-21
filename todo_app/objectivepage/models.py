from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Objective(models.Model):
    object_name = models.CharField('目標名', max_length=255)
    object_category = models.CharField('カテゴリ', max_length=255)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.object_name

    class Meta:
        db_table = 'objective'
        verbose_name = '目標名'
        verbose_name_plural = '目標名'
        unique_together = ('object_name', 'user')
