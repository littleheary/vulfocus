# Generated by Django 2.2.5 on 2019-12-20 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dockerapi', '0016_auto_20191220_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timemoudel',
            name='time_id',
            field=models.CharField(default='f2ae48f4-a4d7-4a0c-a1b0-94f035bef3d9', max_length=255, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
