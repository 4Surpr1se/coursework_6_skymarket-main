from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser


class UserRoles:
    # TODO закончите enum-класс для пользователя
    pass


class User(AbstractBaseUser):
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    objects = UserManager()

    USER = 'user'
    ADMIN = 'admin'

    ROLES = [(USER, USER),
             (ADMIN, ADMIN)]

    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=12, default='')
    password = models.CharField(max_length=100, default='')
    role = models.CharField(max_length=10, choices=ROLES)
    email = models.EmailField(default='', blank=True, unique=True)
    image = models.ImageField(upload_to='images/authors/', null=True, blank=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_admin(self):
        return self.role == self.ADMIN  #

    @property
    def is_user(self):
        return self.role == self.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

