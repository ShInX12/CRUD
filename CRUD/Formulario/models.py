from django.db import models


class Persona(models.Model):
    HOMBRE = 'H'
    MUJER = 'M'

    GENEROS = (
        (HOMBRE, 'Hombre'),
        (MUJER, 'Mujer')
    )

    cc = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=150)
    telefono = models.IntegerField(blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    genero = models.CharField(max_length=2, choices=GENEROS)
    dob = models.DateField()
    bio = models.CharField(blank=True, null=True, default='', max_length=5000)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)

    objetos = models.Manager()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.nombre)


#    def get_absolute_url(self):
#        return reverse('formulario:persona_detail',
#                       args=[self.cc])

class Mascota(models.Model):

    especies =(
        ('Canino', 'Perro'),
        ('Felino', 'Gato'),
        ('Ave', 'Pajaro'),
        ('Pez', 'Pez'),
        ('Exotico','Exotico'),
        ('Otro','Otro')
    )

    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField(blank=True, null=True)
    especie = models.CharField(max_length=6, choices=especies)
    color = models.CharField(max_length=25, blank=True, null=True)

