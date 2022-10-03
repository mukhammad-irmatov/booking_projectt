# from django.core.validators import RegexValidator
#
# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
# from apps.users.managers import MyAccountManager
#
#
# def get_profile_image_filepath(self , filepath):
#     return 'profile_images/' + str(self.pk) + '/profile_image.png'
#
#
# def get_default_profile_image():
#     return "default_prof_pic.jpeg"
#
#
# phone_regex = RegexValidator(
#     regex=r'^998[0-9]{9}$',
#     message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
# )
#
#
# class User(AbstractUser):
#     email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     phone = models.CharField(max_length=200, validators=[phone_regex], unique=True)
#
#     date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#
#     profile_image = models.ImageField(max_length=255, upload_to=get_profile_image_filepath,
#                                       null=True, blank=True, default=get_default_profile_image)
#     # REQUIRED_FIELDS = ["phone", "email"]
#
#     # objects = MyAccountManager()
#
#     def __str__(self):
#         return self.first_name
#
#     def get_profile_image_filename(self):
#         return str(self.profile_image)[str(self.profile_image).index('profile_images/' + str(self.pk) + "/"):]
#
#
