from django.db import models

from .common import CommonModel


class Profile(CommonModel):
    title = models.CharField(max_length=256, blank=True, null=True, )
    phone = models.CharField('Phone Number', max_length=11, unique=True, )
    national_id = models.CharField('National ID', max_length=10, unique=True, )
    address = models.TextField('Address', null=True, blank=True, )
    gender = models.CharField('Gender', null=True, blank=True, max_length=10)
    birthdate = models.DateTimeField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)


    def __str__(self):
        return "{0}".format(self.title)
