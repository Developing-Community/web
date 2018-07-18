from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



def profile_image_upload_location(instance, filename):
    return "user/%s/profile/%s" %(instance.user.id, filename)

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to=profile_image_upload_location,
                                      null=True,
                                      blank=True,
                                      width_field="width_field",
                                      height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()