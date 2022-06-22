from django.db import models

from localflavor.us.models import USStateField


class Community(models.Model):
    name = models.CharField(max_length=100, blank=False)
    payroll_code = models.CharField(max_length=3, null=True, blank=True)
    badge_prefix = models.CharField(max_length=3, null=True, blank=True)
    new_development = models.BooleanField(default=False)
    currently_supported = models.BooleanField(default=False)
    address_1 = models.CharField('address', max_length=128, null=True, blank=True)
    address_2 = models.CharField('address cont', max_length=128, null=True, blank=True)
    city = models.CharField('city', max_length=64, null=True, blank=True)
    state = USStateField('state', null=True, blank=True)
    zip_code = models.CharField('zip code', max_length=5, null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f'{self.name}'
