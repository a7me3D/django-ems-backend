from django import forms
from .models import Employee


class SignupForm(forms.ModelForm):
    class Meta:
        model = Employee

        fields = ["email", "first_name", "last_name", "adresse",
                  "ville", "code_postal", "nationnalite", "date_naissance", "lieu_naissance",
                  "sexe", "cin", "poste", "password"]

        widgets = {
            'password': forms.PasswordInput()
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
