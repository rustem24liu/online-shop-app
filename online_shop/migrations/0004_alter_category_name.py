# Generated by Django 5.0.1 on 2024-02-07 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Category Name'),
        ),
    ]
