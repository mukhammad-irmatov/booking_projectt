from apps.users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    """
    A Custom form for creating new users.
    """

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user
