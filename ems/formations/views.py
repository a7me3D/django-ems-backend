from django.shortcuts import render, reverse

from django.views import generic
from .models import Formation

from users.decorators import allowed_users
from django.utils.decorators import method_decorator


@method_decorator(allowed_users(["RI", "RH", "S", "RF"]), name='dispatch')
class FormationListView(generic.ListView):
    template_name = "formation_view.html"
    context_object_name = "formations"
    model = Formation


@method_decorator(allowed_users(["RH"]), name='dispatch')
class FormationCreationView(generic.CreateView):
    model = Formation
    fields = ["titre", "genre", "jour", "formateur", "duree", "lieu", "sujet"]
    template_name = "formation_create.html"

    def get_success_url(self):
        return reverse("formations:formation-view")


@method_decorator(allowed_users(["RH"]), name='dispatch')
class FormationUpdateView(generic.UpdateView):
    template_name = "formation_update.html"
    queryset = Formation.objects.all()

    fields = ["titre", "genre", "jour", "formateur", "duree", "lieu", "sujet"]

    def get_success_url(self):
        return reverse("formations:formation-view")

    def form_valid(self, form):
        form.save()
        return super(FormationUpdateView, self).form_valid(form)


@method_decorator(allowed_users(["RH"]), name='dispatch')
class FormationDeleteView(generic.DeleteView):
    template_name = "formation_delete.html"
    queryset = Formation.objects.all()

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("formations:formation-view")


@method_decorator(allowed_users(["RI", "RH", "S", "RF"]), name='dispatch')
class FormationDetailView(generic.DetailView):
    model = Formation
    template_name = 'formation_detail.html'
    context_object_name = "formation"
