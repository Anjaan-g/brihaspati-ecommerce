from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

class CustomUser(AbstractUser):
    first_name = models.CharField(_("First Name"), max_length=50)
    last_name = models.CharField(_("Last Name"), max_length=50)
    email = models.EmailField(_("Email"), max_length=254)
    phone_no = models.PhoneNumberField(_("Phone number"))
    address = models.CharField(_("Address"), max_length=100)
    is_admin = models.BooleanField(_("Admin Status"), default=False)

    def __str__(self):
        return f'{self.first_name}+" "{self.last_name}'
    