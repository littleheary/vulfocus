# Generated by Django 2.2.5 on 2019-12-06 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dockerapi', '0007_auto_20191205_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combinationcontainer',
            name='image_id',
            field=models.UUIDField(editable=False, verbose_name='镜像ID'),
        ),
        migrations.AlterField(
            model_name='timemoudel',
            name='time_id',
            field=models.CharField(default='ce7cbda8-491e-4af2-a83a-ca02968a901c', max_length=255, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]