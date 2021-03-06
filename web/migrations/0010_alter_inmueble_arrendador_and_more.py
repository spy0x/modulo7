# Generated by Django 4.0.3 on 2022-04-12 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0009_remove_userprofile_primer_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inmueble',
            name='arrendador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrendador', to='web.userprofile'),
        ),
        migrations.AlterField(
            model_name='inmueble',
            name='arrendatario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='arrendatario', to='web.userprofile'),
        ),
        migrations.AlterField(
            model_name='solicitudarriendo',
            name='user_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.userprofile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
