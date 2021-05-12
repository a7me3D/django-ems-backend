from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic
from .models import Employee

from .forms import SignupForm


class HomeView(LoginRequiredMixin, generic.View):
    login_url = "/auth/login"

    ROLE_BASED_REDIRECT = {
        "S": '',
        "RI": 'users:employee-view',
        "CH": '',
        "RF": '',
        "RH": 'users:user-home',
    }

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            user_role = str(user.poste)
            return HttpResponseRedirect(reverse(self.ROLE_BASED_REDIRECT[user_role]))

        else:
            return HttpResponseRedirect("auth/login")


class EmployeeListView(generic.ListView):
    template_name = "employee_view.html"
    context_object_name = "employees"
    model = Employee

    def get_queryset(self):
        if self.request.user.poste == "RH":
            return Employee.objects.filter(poste="S")
        else:
            return Employee.objects.all()


class ProfileDetailView(generic.DetailView):
    model = Employee
    template_name = 'profile_view.html'
    context_object_name = "employee"

    def get_object(self):
        return Employee.objects.get(pk=self.request.user.id)


class EmployeeCreationView(generic.CreateView):
    model = Employee
    form_class = SignupForm

    template_name = "employee_create.html"

    def get_success_url(self):
        return reverse("users:employee-view")


class EmployeeUpdateView(generic.UpdateView):
    template_name = "employee_update.html"
    queryset = Employee.objects.all()
    form_class = SignupForm

    def get_success_url(self):
        return reverse("users:employee-view")

    def form_valid(self, form):
        form.save()
        return super(EmployeeUpdateView, self).form_valid(form)


class ProfileUpdateView(generic.UpdateView):
    template_name = "employee_update.html"
    queryset = Employee.objects.all()

    fields = ["email", "first_name", "last_name", "adresse",
              "ville", "code_postal", "nationnalite", "date_naissance", "lieu_naissance",
              "sexe", "cin", "chef", "poste"]

    def get_object(self):
        return Employee.objects.get(pk=self.request.user.id)

    def get_success_url(self):
        return reverse("users:employee-view")

    def form_valid(self, form):
        form.save()
        return super(EmployeeUpdateView, self).form_valid(form)


class EmployeeDeleteView(generic.DeleteView):
    template_name = "employee_delete.html"

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("users:employee-view")


class EmployeeActivateView(generic.View):
    def get(self, request, *args, **kwargs):
        user = Employee.objects.get(pk=self.kwargs.get("pk"))
        user.is_active = True
        user.save()
        return HttpResponseRedirect(reverse("users:employee-view"))


class EmployeeDesactivateView(generic.View):
    def get(self, request, *args, **kwargs):
        user = Employee.objects.get(pk=self.kwargs.get("pk"))
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse("users:employee-view"))
