from django.utils.translation import gettext_lazy as _
from django.db import models
from django.db.models import Sum
from django.dispatch import receiver
from django.db.models.signals import pre_save
from ..product.models import Raw, Product
from .constant import *


class RawStock(models.Model):
    name = models.CharField(_("Name"), null=True, blank=True, max_length=150)
    count = models.PositiveIntegerField(default=0)

    # supply_item = models.ForeignKey(ProductStock, on_delete=models.SET_DEFAULT, verbose_name=_("Stock"))
    # order_item = models.ForeignKey(ProductStock, on_delete=models.SET_NULL, verbose_name=_("Stock"))
    raw = models.ForeignKey(Raw, on_delete=models.CASCADE, verbose_name=_("Raw"))
    serial_number = models.CharField(_("Serial Number"), null=True, blank=True, max_length=150)
    status = models.IntegerField(
        _("Stock Item Status"), choices=STOCK_ITEM_STATUS.choices, default=STOCK_ITEM_STATUS.IN_SUPPLY_ORDER
    )
    cost_price = models.DecimalField(_("Cost Price"), default=0.0, decimal_places=2, max_digits=10)

    created_at = models.DateTimeField(_("Created Data"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True, editable=False)

    class Meta:
        verbose_name = _("Raw Material Stock")
        verbose_name_plural = _("Raw Materials Stock")
        db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
        ordering = ("-created_at",)

    def __str__(self):
        return "{}".format(self.name)


class ProductStock(models.Model):
    name = models.CharField(_("Name"), null=True, blank=True, max_length=150)
    count = models.PositiveIntegerField(default=0)

    # supply_item = models.ForeignKey(ProductStock, on_delete=models.SET_DEFAULT, verbose_name=_("Stock"))
    # order_item = models.ForeignKey(ProductStock, on_delete=models.SET_NULL, verbose_name=_("Stock"))
    # raw_stock = models.ForeignKey(RawStock, on_delete=models.SET_NULL, verbose_name=_("Stock"))

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Raw"))
    serial_number = models.CharField(_("Serial Number"), null=True, blank=True, max_length=150)
    status = models.IntegerField(
        _("Stock Item Status"), choices=STOCK_ITEM_STATUS.choices, default=STOCK_ITEM_STATUS.IN_SUPPLY_ORDER
    )
    cost_price = models.DecimalField(_("Cost Price"), default=0.0, decimal_places=2, max_digits=10)

    created_at = models.DateTimeField(_("Created Data"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True, editable=False)

    class Meta:
        verbose_name = _("Product Stock")
        verbose_name_plural = _("Products Stock")
        db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
        ordering = ("-created_at",)

    def __str__(self):
        return "{}".format(self.name)


# @receiver(pre_save, sender=ProductStock)  ###
# def set_product_stock_total(sender, instance, **kwargs):
#     try:
#         instance.count = (
#             instance.count + ProductStock.objects.filter(name=instance.name).aggregate(Sum("count"))["count__sum"]
#         )
#     except:
#         instance.count = 0
