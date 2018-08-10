from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to=profile_image_upload_location,
                                      null=True,
                                      blank=True,
                                      width_field="width_field",
                                      height_field="height_field")
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null=True)
    subscribe_to_newsletter = models.BooleanField(default=True)
    email_publicity = models.BooleanField(default=True)
    applications = models.ManyToManyField(Application, blank=True)
    def __str__(self):
        return str(self.user)


class ContactInfo(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="contact_info")
    info = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.user) + " | " + self.info



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
