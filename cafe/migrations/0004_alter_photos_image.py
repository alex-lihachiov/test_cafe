# Generated by Django 3.2.5 on 2021-07-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0003_auto_20210721_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='image',
            field=models.ImageField(null=True, upload_to='cafe_shots/', verbose_name='Фото интерьера'),
        ),
    ]
