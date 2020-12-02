# Generated by Django 3.0.8 on 2020-08-28 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0002_auto_20200828_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(),
        ),
    ]