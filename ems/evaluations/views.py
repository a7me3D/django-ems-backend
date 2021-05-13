from django.views import generic
from django.shortcuts import reverse
from users.models import Employee
from .models import Evaluation, Criteria, CriteriaType
from .forms import CriteriaFormSet

from users.decorators import allowed_users
from django.utils.decorators import method_decorator


@method_decorator(allowed_users(["RH"]), name='dispatch')
class EvaluationCreationView(generic.CreateView):
    model = Evaluation
    template_name = "evaluation_create.html"
    fields = ["start_period", "end_period"]

    def get_success_url(self):
        return reverse("evaluations:evaluations-view")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # criteria_types = CriteriaType.objects.all()
        initial_types = [{"title": Ctype}
                         for Ctype in CriteriaType.objects.all()]

        employee_id = self.kwargs.get("pk")
        employee = Employee.objects.get(pk=employee_id)
        context['employee'] = employee

        formset = CriteriaFormSet(
            initial=initial_types, queryset=Criteria.objects.none())
        context['formset'] = formset
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.employee = self.request.user
        self.object.evaluator = Employee.objects.get(pk=self.kwargs.get("pk"))
        self.object.save()

        formset = CriteriaFormSet(self.request.POST)
        for cform in formset:
            if cform.is_valid():
                cformid = cform.save()
                self.object.criteria.add(cformid)

        return super(EvaluationCreationView, self).form_valid(form)


@method_decorator(allowed_users(["RI", "RH", "S", "RF"]), name='dispatch')
class EvaluationDetailView(generic.DetailView):
    model = Evaluation
    template_name = 'evaluation_detail.html'
    context_object_name = "evaluation"

    def get_object(self):
        try:
            pk = self.kwargs["pk"]
            evaluation = Evaluation.objects.filter(
                employee=pk).last()

        except:
            evaluation = Evaluation.objects.filter(
                employee=self.request.user.id).last()

        return evaluation


@method_decorator(allowed_users(["RH"]), name='dispatch')
class EvaluationListView(generic.ListView):
    model = Evaluation
    template_name = 'evaluations_view.html'
    context_object_name = "evaluations"


@method_decorator(allowed_users(["RH"]), name='dispatch')
class EvaluationDeleteView(generic.DeleteView):
    template_name = "evaluation_delete.html"
    queryset = Evaluation.objects.all()

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("evaluations:evaluations-view")
