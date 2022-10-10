from django.db import models
from django.utils.translation import gettext_lazy as _

from commons.models.base import Model


class Person(Model):

    name = models.CharField(_("Name"), max_length=100, null=True, blank=True)

    class Meta:
        db_table = "person"
        verbose_name = _("People")
        verbose_name_plural = _("People")
