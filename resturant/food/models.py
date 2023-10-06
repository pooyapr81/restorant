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


class Food(models.Model):
    Food_type = [
        ("breakfast", "breakfast"),
        ("lunch", "lunch"),
        ("dinner", "dinner"),
        ("drinks", "drinks"),
    ]
    name = models.CharField(max_length=100)
    description = models.CharField(_("توضیحات"), max_length=50)
    rate = IntegerRangeField(_("امتیاز"), default=0, min_value=0, max_value=100)
    price = models.IntegerField()
    time = models.IntegerField(_("زمان پخت"))
    pup_date = models.DateTimeField(_("زمان انتشار"), auto_now_add=True)
    photo = models.ImageField(upload_to='foods/', null=True, blank=True)
    type_food = models.CharField(max_length=10, choices=Food_type, default="dinner")
