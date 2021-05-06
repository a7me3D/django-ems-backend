from django.shortcuts import render, reverse

from django.views import generic
from .models import Recruitment


class RecruitmentListView(generic.ListView):
    template_name = "recruitment_view.html"
    context_object_name = "recruitments"
    model = Recruitment


class RecruitmentCreationView(generic.CreateView):
    model = Recruitment
    fields = ["direction", "responsable", "date_demande", "poste", "poste_type",
              "poste_description", "motivation", "exp_requise", "formation_requise"]
    template_name = "recruitment_create.html"

    def get_success_url(self):
        return reverse("recruitments:recruitment-view")


class RecruitmentUpdateView(generic.UpdateView):
    template_name = "recruitment_update.html"
    queryset = Recruitment.objects.all()

    fields = ["direction", "responsable", "date_demande", "poste", "poste_type",
              "poste_description", "motivation", "exp_requise", "formation_requise"]

    def get_success_url(self):
        return reverse("recruitments:recruitment-view")

    def form_valid(self, form):
        form.save()
        return super(RecruitmentUpdateView, self).form_valid(form)


class RecruitmentDeleteView(generic.DeleteView):
    template_name = "recruitment_delete.html"
    queryset = Recruitment.objects.all()

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("recruitments:recruitment-view")


class RecruitmentDetailView(generic.DetailView):
    model = Recruitment
    template_name = 'recruitment_detail.html'
    context_object_name = "recruitment"
