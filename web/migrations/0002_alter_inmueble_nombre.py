# Generated by Django 4.0.3 on 2022-04-06 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
