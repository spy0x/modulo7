# Generated by Django 4.0.3 on 2022-04-06 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=255)),
                ('m2_construidos', models.IntegerField()),
                ('m2_totales', models.IntegerField()),
                ('n_estacionamientos', models.IntegerField()),
                ('n_habitaciones', models.IntegerField()),
                ('n_banos', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('tipo', models.CharField(choices=[('Casa', 'Casa'), ('Departamento', 'Departamento'), ('Parcela', 'Parcela')], default='C', max_length=15)),
                ('precio_mensual', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('type', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('can_admin', models.BooleanField(default=False)),
                ('can_list_inmuebles', models.BooleanField(default=True)),
                ('can_request_inmuebles', models.BooleanField(default=True)),
                ('can_list_propiedades', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('primer_nombre', models.CharField(max_length=50)),
                ('segundo_nombre', models.CharField(default='', max_length=50)),
                ('primer_apellido', models.CharField(max_length=50)),
                ('segundo_apellido', models.CharField(default='', max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web.comuna')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web.region')),
                ('user_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web.usertype')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudArriendo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inmueble_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.inmueble')),
                ('user_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.user')),
            ],
        ),
        migrations.AddField(
            model_name='inmueble',
            name='arrendador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrendador', to='web.user'),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='arrendatario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='arrendatario', to='web.user'),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='comuna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web.comuna'),
        ),
        migrations.AddField(
            model_name='inmueble',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web.region'),
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web.region'),
        ),
    ]
