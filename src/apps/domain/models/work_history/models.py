from django.db import models
from django.utils.translation import gettext_lazy as _

from commons.models.base import Model


class WorkHistory(Model):

    person = models.ForeignKey(
        "domain.Person",
        verbose_name=_("Person"),
        related_name="work_history",
        on_delete=models.DO_NOTHING,
    )
    company = models.ForeignKey(
        "domain.Company",
        verbose_name=_("Company"),
        related_name="work_history",
        on_delete=models.DO_NOTHING,
        null=True
    )
    
    title = models.CharField(_("Title"), max_length=500, null=True, blank=True)
    group_start_date = models.DateField(_("Group Start Date"), null=True)
    group_end_date = models.DateField(_("Group End Date"), null=True)
    

    class Meta:
        db_table = "work_history"
        verbose_name = _("Work History")
        verbose_name_plural = _("Work Histories")
