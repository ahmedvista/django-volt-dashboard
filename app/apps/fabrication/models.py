from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models
from .constant import *
from ..product.models import Raw, Product


class RawForProduction(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name=_("Product"),
        related_name="products",
    )
    raw = models.ForeignKey(
        Raw,
        on_delete=models.CASCADE,
        verbose_name=_("Raw Material"),
        related_name="raws",
    )
    sub_raw = models.ForeignKey(
        Raw,
        on_delete=models.CASCADE,
        verbose_name=_("Sub Raw Material"),
        related_name="sub_raws",
    )
    quantity_per_product = models.IntegerField(_("Quantity Required for Production"), default=1)
    is_produced = models.BooleanField(_("Need Fabrication"), default=False)
    created_at = models.DateTimeField(_("Created Data"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True, editable=False)

    class Meta:
        verbose_name = _("Raw Material for Production")
        verbose_name_plural = _("Raw Materials for Production")
        db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
        ordering = ("-created_at",)

    def __str__(self):
        return "{}".format(self.product)


class ProductionProcess(models.Model):
    RawForProduction = models.ForeignKey(
        RawForProduction,
        on_delete=models.CASCADE,
        verbose_name=_("Raw For Production"),
        related_name="RawForProduction",
    )
    is_parallel = models.BooleanField(_("Parallel Fabrication"), default=False)
    parallel_quantity = models.IntegerField(_("Quantity for Parallel Production"), default=1)
    production_duration = models.DurationField(verbose_name=_("Time Consumed for Production"))
    created_at = models.DateTimeField(_("Created Data"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True, editable=False)

    class Meta:
        verbose_name = _("Production Process")
        verbose_name_plural = _("Production Processes")
        db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
        ordering = ("-created_at",)

    def __str__(self):
        return "{}".format(self.name)
