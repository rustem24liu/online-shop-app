# Generated by Django 5.0.1 on 2024-02-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0005_category_category_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='img'),
        ),
    ]
