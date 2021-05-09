from django import forms
from .models import Criteria, CriteriaType, Evaluation
from django.forms import modelformset_factory


class CriteriaForm(forms.ModelForm):
    # title = forms.ModelChoiceField(queryset=CriteriaType.objects.all())

    def __init__(self, *args, **kwargs):
        super(CriteriaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Criteria
        fields = ("title", "rating", "comment")


CriteriaFormSet = modelformset_factory(
    Criteria, CriteriaForm, fields="__all__", extra=CriteriaType.objects.count())
