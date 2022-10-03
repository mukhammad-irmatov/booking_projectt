from django.contrib.auth.base_user import BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, email, phone, password=None):
        if not email or phone:
            raise ValueError("Users must have a email or phone number")
        user = self.model(
            email=self.normalize_email(email),
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone, password):
        user = self.create_user(
            email=self.normalize_email(email),
            phone=phone,
            password=password,

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user