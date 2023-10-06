from django.db import models
from django.forms import fields
from django.utils.translation import gettext as _


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Reservation(models.Model):
    name = models.CharField(_("name & family"), max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=11)
    number = IntegerRangeField(_("number of person"), default=1, min_value=1, max_value=30)
    date = models.DateField(auto_now_add=False, auto_now=False)
    time = models.TimeField(auto_now_add=False, auto_now=False)
