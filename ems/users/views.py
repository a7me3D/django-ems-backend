from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic
from .models import Employee

from .forms import SignupForm
from .decorators import allowed_users
from django.utils.decorators import method_decorator


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "home.html"


@method_decorator(allowed_users(["RI", "RH"]), name='dispatch')
class EmployeeListView(generic.ListView):
    template_name = "employee_view.html"
    context_object_name = "employees"
    model = Employee

    def get_queryset(self):
        return Employee.objects.all()


@method_decorator(allowed_users(["RI", "RH", "S", "RF"]), name='dispatch')
class ProfileDetailView(generic.DetailView):
    model = Employee
    template_name = 'profile_view.html'
    context_object_name = "employee"

    def get_object(self):
        return Employee.objects.get(pk=self.request.user.id)


@method_decorator(allowed_users(["RI"]), name='dispatch')
class EmployeeCreationView(generic.CreateView):
    model = Employee
    form_class = SignupForm

    template_name = "employee_create.html"

    def get_success_url(self):
        return reverse("users:employee-view")


@method_decorator(allowed_users(["RI"]), name='dispatch')
class EmployeeUpdateView(generic.UpdateView):
    template_name = "employee_update.html"
    queryset = Employee.objects.all()
    form_class = SignupForm

    def get_success_url(self):
        return reverse("users:employee-view")

    def form_valid(self, form):
        form.save()
        return super(EmployeeUpdateView, self).form_valid(form)


@method_decorator(allowed_users(["RI", "RH", "S", "RF"]), name='dispatch')
class ProfileUpdateView(generic.UpdateView):
    template_name = "employee_update.html"
    queryset = Employee.objects.all()

    fields = ["email", "first_name", "last_name", "adresse",
              "ville", "code_postal", "nationnalite", "date_naissance", "lieu_naissance",
              "sexe", "cin", "poste"]

    def get_object(self):
        return Employee.objects.get(pk=self.request.user.id)

    def get_success_url(self):
        return reverse("users:profile-detail")


@method_decorator(allowed_users(["RI"]), name='dispatch')
class EmployeeDeleteView(generic.DeleteView):
    template_name = "employee_delete.html"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("users:employee-view")


@method_decorator(allowed_users(["RI"]), name='dispatch')
class EmployeeActivateView(generic.View):
    def get(self, request, *args, **kwargs):
        user = Employee.objects.get(pk=self.kwargs.get("pk"))
        user.is_active = True
        user.save()
        return HttpResponseRedirect(reverse("users:employee-view"))


@method_decorator(allowed_users(["RI"]), name='dispatch')
class EmployeeDesactivateView(generic.View):
    def get(self, request, *args, **kwargs):
        user = Employee.objects.get(pk=self.kwargs.get("pk"))
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse("users:employee-view"))
