from django import forms
from .models import Persona, Mascota


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['cc', 'nombre', 'telefono', 'email', 'genero', 'dob', 'bio']

        labels = {'cc': 'Documento de identidad',
                  'nombre': 'Nombre',
                  'telefono': 'Teléfono',
                  'email': 'Correo electrónico',
                  'genero': 'Genero',
                  'dob': 'Fecha de nacimiento',
                  'bio': 'Biografía',
                  }

        widgets = {
            'cc': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel', 'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'autocomplete': 'off'}),
            'genero': forms.Select(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'autocomplete': 'off'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'autocomplete': 'off', 'placeholder': 'Dí algo sobre tí...'}),
        }


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = [
            'persona', 'nombre', 'edad', 'especie', 'color'
        ]

        labels = {
            'persona': 'Dueño',
            'nombre': 'Nombre de la mascota',
            'edad': 'Edad',
            'especie': 'Especie',
            'color': 'Color'
        }

        widgets = {
            'persona': forms.Select(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'edad': forms.TextInput(attrs={'class': 'form-control', 'type': 'number',
                                           'autocomplete': 'off', 'min':'0', 'max': '100'}),
            'especie': forms.Select(attrs={'class': 'form-control', 'autocomplete': 'off'}),
            'color': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off', 'type': 'color'})
        }
