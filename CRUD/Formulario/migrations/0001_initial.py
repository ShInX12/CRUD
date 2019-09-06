# Generated by Django 2.1.7 on 2019-03-13 17:26

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=150)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('genero', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer')], max_length=2)),
                ('dob', models.DateTimeField()),
                ('bio', models.CharField(blank=True, default='', max_length=5000, null=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('id',),
            },
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
    ]
