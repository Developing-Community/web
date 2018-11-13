from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from sorl.thumbnail import ImageField

from companions.models import Application


def profile_image_upload_location(instance, filename):
    return "user/%s/profile/%s" % (instance.user.id, filename)


# class MyUserManager(BaseUserManager):
#     def create_user(self, email, firstname, lastname, username, password=None):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')
#
#         user = self.model(
#             email=self.normalize_email(email),
#             firstname=firstname,
#             lastname=lastname,
#             username=username,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, username, first_name, last_name, password):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(
#             email,
#             first_name=first_name,
#             last_name=last_name,
#             username=username,
#             password=password,
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="profile")

    # for if profile wasn't still registered as user
    first_name = models.CharField(blank=True, null=True, max_length=255)
    last_name = models.CharField(blank=True, null=True, max_length=255)

    # in case we enter compelete name
    complete_name = models.CharField(blank=True, null=True, max_length=255)

    # temp
    phone = models.CharField(blank=True, null=True, max_length=20)

    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = ImageField(upload_to=profile_image_upload_location,
                               null=True,
                               blank=True,
                               width_field="width_field",
                               height_field="height_field")
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null=True)
    subscribe_to_newsletter = models.BooleanField(default=True)
    email_publicity = models.BooleanField(default=True)
    applications = models.ManyToManyField(Application, blank=True)

    telegram_user_id = models.IntegerField(blank=True, null=True, unique=True)

    @property
    def name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return str(self.user)


class ContactInfo(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="contact_info")
    info = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.user) + " | " + self.info


def create_user_profile(sender, instance, created, **kwargs):
    if created and not Profile.objects.filter(user=instance).exists():
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User, dispatch_uid="create_user_profile")
