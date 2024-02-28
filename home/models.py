# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class All Bills(models.Model):

    #__All Bills_FIELDS__
    bill_id = models.CharField(max_length=255, null=True, blank=True)

    #__All Bills_FIELDS__END

    class Meta:
        verbose_name        = _("All Bills")
        verbose_name_plural = _("All Bills")


class Cong_Rep_Bills(models.Model):

    #__Cong_Rep_Bills_FIELDS__
    bill_id = models.CharField(max_length=255, null=True, blank=True)

    #__Cong_Rep_Bills_FIELDS__END

    class Meta:
        verbose_name        = _("Cong_Rep_Bills")
        verbose_name_plural = _("Cong_Rep_Bills")


class User(models.Model):

    #__User_FIELDS__
    f_name = models.CharField(max_length=255, null=True, blank=True)
    l_name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    permissions = models.CharField(max_length=255, null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")



#__MODELS__END
