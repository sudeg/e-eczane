# Generated by Django 3.0.5 on 2020-04-15 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default='Hurry up motherfucker'),
        ),
    ]
