from django.shortcuts import reverse, HttpResponseRedirect
from django.views import generic
from .models import FinanceDoc as Finance

from users.decorators import allowed_users
from django.utils.decorators import method_decorator

@method_decorator(allowed_users(["RI", "RH", "S", "RF"]), name='dispatch')
class FinanceListView(generic.ListView):
    model = Finance
    template_name = 'finance_view.html'
    context_object_name = "finances"

    def get_queryset(self):
        if self.request.user.poste == "RF":
            return Finance.objects.all()
        else:
            return Finance.objects.filter(employee=self.request.user)


@method_decorator(allowed_users(["RI", "RH", "S", "RF"]), name='dispatch')
class FinanceCreationView(generic.CreateView):
    model = Finance
    template_name = "finance_create.html"
    fields = ["doc_type", "montant", "motif",
              "nb_echeances", "avis_rf", ]

    def get_success_url(self):
        return reverse("finances:finance-view")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.employee = self.request.user
        self.object.save()
        return super(FinanceCreationView, self).form_valid(form)


@method_decorator(allowed_users(["RI", "RH", "S", "RF"]), name='dispatch')
class FinanceDetailView(generic.DetailView):
    model = Finance
    template_name = 'finance_detail.html'
    context_object_name = "finance"


@method_decorator(allowed_users(["RI", "RH", "S", "RF"]), name='dispatch')
class FinanceUpdateView(generic.UpdateView):
    model = Finance
    template_name = "finance_update.html"
    fields = ["doc_type", "montant", "motif",
              "nb_echeances", "avis_rf", ]

    def get_success_url(self):
        return reverse("finances:finance-view")


@method_decorator(allowed_users(["RI", "RH", "S", "RF"]), name='dispatch')
class FinanceDeleteView(generic.DeleteView):
    template_name = "formation_delete.html"
    queryset = Finance.objects.all()

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("finances:finance-view")


@method_decorator(allowed_users(["RF"]), name='dispatch')
class FinanceAcceptView(generic.View):
    def get(self, request, *args, **kwargs):
        doc = Finance.objects.get(pk=self.kwargs.get("pk"))
        doc.status = dict(Finance.STATUS_TYPE).get("A")
        doc.save()
        return HttpResponseRedirect(reverse("finances:finance-view"))


@method_decorator(allowed_users(["RF"]), name='dispatch')
class FinanceRejectView(generic.View):
    def get(self, request, *args, **kwargs):
        doc = Finance.objects.get(pk=self.kwargs.get("pk"))
        doc.status = dict(Finance.STATUS_TYPE).get("R")
        doc.save()
        return HttpResponseRedirect(reverse("finances:finance-view"))
