from django.contrib.auth.backends import ModelBackend, UserModel
from django.db.models import Q
from .models import Employee


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:  # to allow authentication through phone number or any other field, modify the below statement
            user = UserModel.objects.get(email__iexact=username)
            print("user:", user)
        except UserModel.DoesNotExist:
            print(username, ' does not exist')
            UserModel().set_password(password)
        else:
            print(password, user.check_password(password))
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

        return user if self.user_can_authenticate(user) else None
