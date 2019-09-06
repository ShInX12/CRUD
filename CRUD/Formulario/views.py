from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import PersonaForm, MascotaForm
from .models import Persona, Mascota


def lista_personas(request):
    personas = Persona.objetos.all()
    contexto = {'personas': personas}
    return render(request, 'CRUD/list.html', contexto)


def editar_persona(request, cc):
    persona = Persona.objetos.get(cc=cc)
    if request.method == 'GET':
        form = PersonaForm(instance=persona)
    else:
        form = PersonaForm(request.POST, instance=persona)
        if form.is_valid():
            form.save()
        return redirect('persona:lista_personas')
    return render(request, 'CRUD/form.html',
                  {'form': form})


def eliminar_persona(request, cc):
    persona = Persona.objetos.get(cc=cc)
    if request.method == 'POST':
        persona.delete()
        return redirect('persona:lista_personas')
    return render(request, 'CRUD/eliminar_persona.html',
                  {'persona': persona})


def crear_persona(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            nueva_persona = form.save(commit=False)
            nueva_persona.save()
        return redirect('persona:lista_personas')
    else:
        form = PersonaForm()
    return render(request, 'CRUD/form.html',
                  {'form': form})


class ListaPersonas(ListView):
    model = Persona
    template_name = 'CRUD/list.html'
    paginate_by = 10


class CrearPersona(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'CRUD/form.html'
    success_url = reverse_lazy('persona:lista_personas')


class EditarPersona(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'CRUD/form.html'
    success_url = reverse_lazy('persona:lista_personas')


class EliminarPersona(DeleteView):
    model = Persona
    template_name = 'CRUD/eliminar_persona.html'
    success_url = reverse_lazy('persona:lista_personas')


class ListaMascotas(ListView):
    model = Mascota
    template_name = 'CRUD/list_mascotas.html'
    paginate_by = 10


class CrearMascota(CreateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'CRUD/form_mascota.html'
    success_url = reverse_lazy('persona:lista_mascotas')


class EditarMascota(UpdateView):
    model = Mascota
    form_class = MascotaForm
    template_name = 'CRUD/form_mascota.html'
    success_url = reverse_lazy('persona:lista_mascotas')


class EliminarMascota(DeleteView):
    model = Mascota
    template_name = 'CRUD/eliminar_persona.html'
    success_url = reverse_lazy('persona:lista_mascotas')

# class CrearMascota(CreateView):
#     model = Mascota
#     template_name = 'CRUD/Formulario/form_mascota.html'
#     form_class = MascotaForm
#     second_form_class = PersonaForm
#     success_url = reverse_lazy('persona:lista_mascotas')
#
#     def get_context_data(self, **kwargs):
#         context = super(CrearMascota, self).get_context_data(**kwargs)
#         if 'form' not in context:
#             context['form'] = self.form_class(self.request.GET)
#         if 'form2' not in context:
#             context['form2'] = self.second_form_class(self.request.GET)
#         return context
#
#     def post(self, request, *args, **kwargs):
#         self.object = self.get_object
#         form = self.form_class(request.POST)
#         form2 = self.second_form_class(request.POST)
#         if form.is_valid() and form2.is_valid():
#             mascota = form.save()
#             mascota.persona = form2.save()
#             mascota.save()
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return self.render_to_response(self.get_context_data(form=form, form2=form2))
