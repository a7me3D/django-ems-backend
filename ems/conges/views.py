from django.shortcuts import reverse, HttpResponseRedirect, get_object_or_404
from django.views import generic
from .models import Conge, CongeTitle


class CongeListView(generic.ListView):
    model = Conge
    template_name = 'conge_view.html'
    context_object_name = "conges"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        conge_count = CongeTitle.objects.filter(
            conge__employee=self.request.user).count()
        print(conge_count)
        if conge_count > 0:
            context["solde"] = CongeTitle.objects.last().rest
        else:
            context["solde"] = 30

        return context

    def get_queryset(self):
        if self.request.user.poste == "RH":
            return Conge.objects.all()

        return Conge.objects.filter(employee=self.request.user)


class CongeCreationView(generic.CreateView):
    model = Conge
    template_name = "conge_create.html"
    fields = ["start_date", "end_date", "conge_type"]

    def get_success_url(self):
        return reverse("conges:conge-view")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.employee = self.request.user
        self.object.save()
        return super(CongeCreationView, self).form_valid(form)


class CongeDetailView(generic.DetailView):
    model = Conge
    template_name = 'conge_detail.html'
    context_object_name = "conge"


class CongeUpdateView(generic.UpdateView):
    model = Conge
    template_name = "conge_update.html"
    fields = ["start_date", "end_date", "conge_type"]

    def get_success_url(self):
        return reverse("conges:conge-view")


class CongeDeleteView(generic.DeleteView):
    template_name = "conge_delete.html"
    queryset = Conge.objects.all()

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("conges:conge-view")


class CongeAcceptView(generic.CreateView):
    model = CongeTitle
    template_name = "conge_accept.html"
    fields = ["interim"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["conge"] = Conge.objects.get(pk=self.kwargs.get("pk"))
        conge_count = CongeTitle.objects.filter(
            conge__employee=self.request.user).count()
        if conge_count > 0:
            context["solde"] = CongeTitle.objects.last().solde
        else:
            context["solde"] = 30
        context["reste"] = context["solde"] - context["conge"].days
        return context

    def form_valid(self, form):
        conge = Conge.objects.get(pk=self.kwargs.get("pk"))
        conge_title = form.save(commit=False)
        conge.status = dict(Conge.STATUS_TYPE).get("A")
        conge_title.conge = conge
        conge.save()

        conge_count = CongeTitle.objects.filter(
            conge__employee=conge.employee).count()
        if conge_count > 0:
            last_conge = CongeTitle.objects.filter(
                conge__employee=conge.employee).last()
            conge_title.solde = last_conge.rest
        conge_title.save()
        return HttpResponseRedirect(reverse("conges:conge-view"))


class CongeRejectView(generic.View):
    def get(self, request, *args, **kwargs):
        doc = Conge.objects.get(pk=self.kwargs.get("pk"))
        doc.status = dict(Conge.STATUS_TYPE).get("R")
        doc.save()
        return HttpResponseRedirect(reverse("conges:conge-view"))
