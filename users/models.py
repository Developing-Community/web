from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from learningFields.models import LearningField


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, learning_fields_desc, bio, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            learning_fields_desc=learning_fields_desc,
            username=username,
            bio=bio,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, learning_fields_desc, password, bio):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            learning_fields_desc=learning_fields_desc,
            username=username,
            bio=bio,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    bio = models.TextField()
    learning_fields = models.ManyToManyField(LearningField, related_name='user_learning_fields')
    learning_fields_desc = models.TextField()
    guiding_fields = models.ManyToManyField(LearningField, related_name='user_guiding_fields')
    objects = MyUserManager()
    username = models.CharField(
        max_length=255,
        unique=True,
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'bio', 'learning_fields_desc']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
