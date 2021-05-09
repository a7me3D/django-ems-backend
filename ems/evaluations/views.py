from django.shortcuts import render, HttpResponse
from django.views import generic
from .models import Evaluation, Criteria, CriteriaType
from .forms import CriteriaForm, CriteriaFormSet


class EvaluationCreationView(generic.CreateView):
    model = Evaluation
    template_name = "evaluation_create.html"
    fields = ["start_period", "end_period"]
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        criteria_types = CriteriaType.objects.all()
        initial_types = [{"title": Ctype}
                         for Ctype in CriteriaType.objects.all()]

        formset = CriteriaFormSet(
            initial=initial_types, queryset=Criteria.objects.none())
        context['formset'] = formset
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.employee = self.request.user
        self.object.evaluator = self.request.user
        self.object.save()

        formset = CriteriaFormSet(self.request.POST)
        for cform in formset:
            if cform.is_valid():
                cformid = cform.save()
                self.object.criteria.add(cformid)
            else:
                print('nope')

        return super(EvaluationCreationView, self).form_valid(form)
