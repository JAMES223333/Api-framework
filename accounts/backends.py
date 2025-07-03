from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()


class UsernameEmailPhoneBackend(ModelBackend):
    def authenticate(self, request, username =None, password = None, **kwargs):
        try:
            user = UserModel.objects.get(
                Q(username___iexact=username) |
                Q(email___iexact=username)    |
                Q(phone___iexact=username)
                
            )
        except UserModel.DoesNotExist:
            return None
        
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
 