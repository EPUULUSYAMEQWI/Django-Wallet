from distutils.command.build_scripts import first_line_re
from email.headerregistry import Address
from operator import ge
from pyexpat import native_encoding
from sys import last_traceback
from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    gender = models.CharField(max_length=15)
    Address = models.Textfield(Address, blank=True)
    age= models.CharField(max_length=2)
    nationality= models.Charfield()
    phone_number= models.CharField(max_length=10)
    email= models.EmailField(max_length=50)