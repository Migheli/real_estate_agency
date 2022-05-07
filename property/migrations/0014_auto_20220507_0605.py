# Generated by Django 2.2.24 on 2022-05-07 03:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20220507_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliamed_flats', to=settings.AUTH_USER_MODEL, verbose_name='Кто пожаловался'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claims', to='property.Flat', verbose_name='Квартира, на которую пожаловались'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='likes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='liked_flats', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]