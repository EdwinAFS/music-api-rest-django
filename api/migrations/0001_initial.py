# Generated by Django 2.2.7 on 2019-11-15 04:17

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=2)),
                ('fecha_nacimiento', models.DateField()),
                ('pais_nacimiento', django_countries.fields.CountryField(max_length=2)),
                ('nacionalidad', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=60)),
                ('fecha_lanzamiento', models.DateField(auto_now=True)),
                ('sello_discografico', models.CharField(max_length=60)),
                ('ranking', models.SmallIntegerField()),
                ('imagen', models.URLField()),
                ('clasificacion', models.CharField(choices=[('CLA', 'Clásica'), ('MOD', 'Moderna'), ('CUL', 'Culta'), ('TRA', 'Tradicional'), ('ELE', 'Electrónica'), ('INS', 'Instrumental')], max_length=3)),
                ('video', models.URLField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Album')),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Artista')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=6, unique=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=6, unique=True)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ListaReproduccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
                ('canciones', models.ManyToManyField(to='api.Cancion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='cancion',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Genero'),
        ),
        migrations.AddField(
            model_name='cancion',
            name='idioma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.Idioma'),
        ),
        migrations.AddField(
            model_name='artista',
            name='generos',
            field=models.ManyToManyField(to='api.Genero'),
        ),
    ]
