# Generated by Django 2.1.7 on 2019-04-04 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Formulario', '0002_auto_20190328_1257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('especie', models.CharField(choices=[('Canino', 'Perro'), ('Felino', 'Gato'), ('Ave', 'Pajaro'), ('Pez', 'Pez'), ('Exotico', 'Exotico'), ('Otro', 'Otro')], max_length=6)),
                ('color', models.CharField(blank=True, max_length=25, null=True)),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Formulario.Persona')),
            ],
        ),
    ]