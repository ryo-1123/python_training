# Generated by Django 2.2 on 2020-04-20 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('objectivepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_name', models.CharField(max_length=255, verbose_name='行動目標名')),
                ('target_content', models.CharField(max_length=255, verbose_name='内容')),
                ('target_status', models.IntegerField(verbose_name='学習ステータス')),
                ('expectation_time', models.IntegerField(verbose_name='予想時間')),
                ('actual_time', models.IntegerField(verbose_name='実際時間')),
                ('understanding_level', models.IntegerField(verbose_name='理解度')),
                ('objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objectivepage.Objective')),
            ],
            options={
                'verbose_name': '行動目標名',
                'verbose_name_plural': '行動目標名',
                'db_table': 'target',
            },
        ),
    ]