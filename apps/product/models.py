from django.utils.translation import gettext_lazy as _
from django.db import models


class Raw(models.Model):
    name = models.CharField(_("Name"), null=True, blank=True, max_length=150)
    sale_price = models.DecimalField(
        _("Sale Price"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
    )
    is_saleable = models.BooleanField(_("Saleable"), default=False)
    created_at = models.DateTimeField(_("Created Data"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True, editable=False)

    class Meta:
        verbose_name = _("Raw Material")
        verbose_name_plural = _("Raw Materials")
        db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
        ordering = ("-created_at",)

    def __str__(self):
        return "{}".format(self.name)


class Product(models.Model):
    name = models.CharField(_("Name"), null=True, blank=True, max_length=150)
    sale_price = models.DecimalField(_("Sale Price"), null=True, blank=True, decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(_("Created Data"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True, editable=False)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
        ordering = ("-created_at",)

    def __str__(self):
        return "{}".format(self.name)


class ProductAttr(models.Model):
    product = models.ForeignKey(Product, related_name="ProductAttr", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=500)

    class Meta:
        verbose_name = _("Product Attributes")
        verbose_name_plural = _("Product Attributes")
        db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")

    def __str__(self):
        return f"{self.name} - {self.value}"
