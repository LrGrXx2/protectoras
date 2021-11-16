# Generated by Django 3.2.9 on 2021-11-16 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=200, verbose_name='Especie')),
                ('nombre_raza', models.CharField(max_length=200, verbose_name='Raza')),
                ('descripcion_animal', models.CharField(blank=True, max_length=500, verbose_name='Descripción general')),
            ],
            options={
                'verbose_name': 'Animal',
                'verbose_name_plural': 'Animales',
            },
        ),
        migrations.CreateModel(
            name='Protectora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_protectora', models.CharField(max_length=200, verbose_name='Nombre protectora')),
                ('direccion', models.CharField(blank=True, max_length=200, verbose_name='Dirección')),
                ('ciudad', models.CharField(blank=True, max_length=200, verbose_name='Ciudad')),
                ('coordenadas', models.CharField(blank=True, max_length=500, verbose_name='Coordenadas')),
            ],
            options={
                'verbose_name': 'Protectora',
                'verbose_name_plural': 'Protectoras',
            },
        ),
        migrations.CreateModel(
            name='Rescate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_animal', models.CharField(max_length=200, verbose_name='Nombre animal')),
                ('adoptado', models.CharField(max_length=200, verbose_name='En adopción')),
                ('descripcion_rescate', models.CharField(blank=True, max_length=500, verbose_name='Descripción de este animal')),
                ('especie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Especie del animal+', to='catalogo.animal')),
                ('nombre_protectora', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.protectora')),
                ('nombre_raza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Raza del animal+', to='catalogo.animal')),
            ],
            options={
                'verbose_name': 'Rescate',
                'verbose_name_plural': 'Rescates',
            },
        ),
    ]