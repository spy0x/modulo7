# Generated by Django 4.0.3 on 2022-04-08 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_remove_usertype_can_admin_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InmuebleType',
            fields=[
                ('type', models.CharField(max_length=25, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web.inmuebletype'),
        ),
    ]
