from django.db import models
from django.utils.translation import gettext_lazy as _

from commons.models.base import Model


class Company(Model):
    
    name = models.CharField(_("Name"), max_length=500, null=True, blank=True)
    linkedin_names = models.CharField(_("Linkedin Names"), max_length=1000, null=True, blank=True)
    description = models.CharField(_("Description"), max_length=10000, null=True, blank=True)
    head_count = models.FloatField(_("Head Count"), null=True, blank=True)
    founding_date = models.DateField(_("Founding Date"), null=True)
    most_recent_raise = models.FloatField(_("Recent Raise"), null=True, blank=True)
    most_recent_valuation = models.FloatField(_("Recent Valuation"), null=True, blank=True)
    investors = models.CharField(_("Investors"), max_length=3000, null=True, blank=True)
    know_total_funding = models.FloatField(_("Recent Valuation"), null=True, blank=True)

    class Meta:
        db_table = "company"
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")
