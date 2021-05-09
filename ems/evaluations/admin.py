from django.contrib import admin
from .models import Evaluation, Criteria, CriteriaType
# Register your models here.

admin.site.register(Evaluation)
admin.site.register(Criteria)
admin.site.register(CriteriaType)
