# Generated by Django 4.0.3 on 2022-04-06 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_inmueble_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='tipo',
            field=models.CharField(choices=[('Casa', 'Casa'), ('Departamento', 'Departamento'), ('Parcela', 'Parcela')], default='Casa', max_length=15),
        ),
    ]