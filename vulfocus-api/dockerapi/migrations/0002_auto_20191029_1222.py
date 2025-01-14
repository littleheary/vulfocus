# Generated by Django 2.2.5 on 2019-10-29 04:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dockerapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageinfo',
            name='image_id',
            field=models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='timemoudel',
            name='time_id',
            field=models.UUIDField(default=uuid.uuid1, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
