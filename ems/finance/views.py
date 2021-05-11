from django.shortcuts import reverse, HttpResponseRedirect
from django.views import generic
from .models import FinanceDoc as Finance


class FinanceListView(generic.ListView):
    model = Finance
    template_name = 'finance_view.html'
    context_object_name = "finances"


class FinanceEmployeeListView(generic.ListView):
    model = Finance
    template_name = 'finance_view.html'
    context_object_name = "finances"

    def get_queryset(self):
        return Finance.objects.filter(employee=self.request.user)


class FinanceCreationView(generic.CreateView):
    model = Finance
    template_name = "finance_create.html"
    fields = ["doc_type", "montant", "motif",
              "nb_echeances", "avis_chef", "avis_rf", ]

    def get_success_url(self):
        return reverse("finances:finance-employee")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.employee = self.request.user
        self.object.save()
        return super(FinanceCreationView, self).form_valid(form)


class FinanceDetailView(generic.DetailView):
    model = Finance
    template_name = 'finance_detail.html'
    context_object_name = "finance"


class FinanceUpdateView(generic.UpdateView):
    model = Finance
    template_name = "finance_update.html"
    fields = ["doc_type", "montant", "motif",
              "nb_echeances", "avis_chef", "avis_rf", ]

    def get_success_url(self):
        return reverse("finances:finance-employee")


class FinanceDeleteView(generic.DeleteView):
    template_name = "formation_delete.html"
    queryset = Finance.objects.all()

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("finances:finance-employee")


class FinanceAcceptView(generic.View):
    def get(self, request, *args, **kwargs):
        doc = Finance.objects.get(pk=self.kwargs.get("pk"))
        doc.status = dict(Finance.STATUS_TYPE).get("A")
        doc.save()
        return HttpResponseRedirect(reverse("finances:finance-view"))


class FinanceRejectView(generic.View):
    def get(self, request, *args, **kwargs):
        doc = Finance.objects.get(pk=self.kwargs.get("pk"))
        doc.status = dict(Finance.STATUS_TYPE).get("R")
        doc.save()
        return HttpResponseRedirect(reverse("finances:finance-view"))
