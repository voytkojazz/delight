# Generated by Django 4.1.1 on 2022-09-09 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_ingridient_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingridient',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]