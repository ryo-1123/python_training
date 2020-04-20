from django.db import models


class Target(models.Model):
    target_name = models.CharField('行動目標名', max_length=255)
    target_content = models.CharField('内容', max_length=255)
    target_status = models.IntegerField('学習ステータス')
    expectation_time = models.IntegerField('予想時間')
    actual_time = models.IntegerField('実際時間')
    understanding_level = models.IntegerField('理解度')
    objective = models.ForeignKey(
        'objectivepage.Objective',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.target_name

    class Meta:
        db_table = 'target'
        verbose_name = '行動目標名'
        verbose_name_plural = '行動目標名'
