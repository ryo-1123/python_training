from django.db import models


class Target(models.Model):
    target_name = models.CharField('行動目標名', max_length=255)
    target_content = models.TextField('内容', max_length=1000, null=True)
    STATUS = (
        (1, '未着手'),
        (2, '進行中'),
        (3, '終了'),
        )
    target_status = models.IntegerField(
        '学習ステータス',
        choices=STATUS,
        default=1,
        )
    expectation_time = models.DurationField('予想時間')
    actual_time = models.DurationField('実際時間', null=True)
    LEVEL = (
        (1, '全然'),
        (2, '何となく'),
        (3, '大体わかった'),
        (4, '結構わかった'),
        (5, '完璧'),
    )
    understanding_level = models.IntegerField(
        '理解度',
        choices=LEVEL,
        default=1,
        )
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
