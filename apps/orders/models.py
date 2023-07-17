from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db import models
from .constant import *
from ..stock.models import RawStock, ProductStock
from decimal import Decimal


class Client(models.Model):
    email = models.EmailField(_("Email"), unique=True, null=False, blank=False)
    name = models.CharField(_("First Name"), null=True, blank=True, max_length=150)
    surname = models.CharField("Last Name", null=True, blank=True, max_length=75)
    phone = models.CharField("Phone", null=True, blank=True, max_length=75)
    address = models.CharField("Address", null=True, blank=True, max_length=140)
    company = models.CharField("Company", null=True, blank=True, max_length=140)
    created_at = models.DateTimeField(_("Created Data"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True, editable=False)

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")
        db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
        ordering = ("-created_at",)

    def __str__(self):
        return "{}".format(self.name)


class Order(models.Model):
    client = models.ForeignKey(
        Client,
        verbose_name=_("Customer"),
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )
    order_title = models.CharField(_("Order Title"), null=True, blank=True, max_length=150)
    status = models.IntegerField(
        _("Order Status"), choices=ORDER_ITEM_STATUS.choices, default=ORDER_ITEM_STATUS.PENDING
    )
    delivery_date = models.CharField(_("Delivery Date"), null=True, blank=True, max_length=150)
    created_at = models.DateTimeField(_("Created Data"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True, editable=False)
    data = models.JSONField(blank=True, null=True)
    total = models.DecimalField(
        _("Total Price"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
    )

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
        ordering = ("-created_at",)

    def __str__(self):
        return "{}".format(self.order_title)


class ProductOrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name=_("Order"),
        on_delete=models.CASCADE,
    )
    product_stock = models.ForeignKey(
        ProductStock,
        verbose_name=_("Product Stock"),
        on_delete=models.CASCADE,
    )
    quantity = models.DecimalField(
        _("Order Quantity"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
        default=Decimal(1),
    )
    actual_quantity = models.DecimalField(
        _("Fulfilled Order Quantity"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
        default=Decimal(0),
    )
    total_cost = models.DecimalField(
        _("Total Cost Price"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
    )
    total_sale = models.DecimalField(
        _("Total Sale Price"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
    )
    total_profit = models.DecimalField(
        _("Total Profit"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
    )
    created_at = models.DateTimeField(_("Created Data"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("updated Data"), auto_now=True, editable=False)

    class Meta:
        verbose_name = _("Product Order Item")
        verbose_name_plural = _("Product Order Items")
        db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
        ordering = ("-created_at",)

    def __str__(self):
        return "{}".format(self.order.order_title)


class RawOrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        verbose_name=_("Order"),
        on_delete=models.CASCADE,
    )
    raw_stock = models.ForeignKey(
        RawStock,
        verbose_name=_("Raw Stock"),
        on_delete=models.CASCADE,
    )
    quantity = models.DecimalField(
        _("Order Quantity"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
        default=Decimal(1),
    )
    actual_quantity = models.DecimalField(
        _("Fulfilled Order Quantity"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
        default=Decimal(0),
    )
    total_cost = models.DecimalField(
        _("Total Cost Price"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
    )
    total_sale = models.DecimalField(
        _("Total Sale Price"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
    )
    total_profit = models.DecimalField(
        _("Total Profit"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
    )
    created_at = models.DateTimeField(_("Created Data"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("updated Data"), auto_now=True, editable=False)

    class Meta:
        verbose_name = _("Raw Order Item")
        verbose_name_plural = _("Raw Order Items")
        db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
        ordering = ("-created_at",)

    def __str__(self):
        return "{}".format(self.order.order_title)


class Supplier(models.Model):
    email = models.EmailField(_("Email"), unique=True, null=False, blank=False)
    name = models.CharField(_("First Name"), null=True, blank=True, max_length=150)
    surname = models.CharField("Last Name", null=True, blank=True, max_length=75)
    phone = models.CharField("Phone", null=True, blank=True, max_length=75)
    address = models.CharField("Address", null=True, blank=True, max_length=140)
    company = models.CharField("Company", null=True, blank=True, max_length=140)
    created_at = models.DateTimeField(_("Created Data"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated Date"), auto_now=True, editable=False)

    class Meta:
        verbose_name = _("Supplier")
        verbose_name_plural = _("Suppliers")
        db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
        ordering = ("-created_at",)

    def __str__(self):
        return "{}".format(self.name)


class SupplyOrder(models.Model):
    supplier = models.ForeignKey(
        Supplier,
        verbose_name=_("Supplier"),
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )
    order_title = models.CharField(_("Order Title"), null=True, blank=True, max_length=150)
    status = models.IntegerField(
        _("Order Status"), choices=ORDER_ITEM_STATUS.choices, default=ORDER_ITEM_STATUS.PENDING
    )
    delivery_date = models.CharField(_("Delivery Date"), null=True, blank=True, max_length=150)
    created_at = models.DateTimeField(_("Created Data"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("updated Data"), auto_now=True, editable=False)
    data = models.JSONField(blank=True, null=True)
    total = models.DecimalField(
        _("Total Price"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
    )

    class Meta:
        verbose_name = _("Supply Order")
        verbose_name_plural = _("Supply Orders")
        db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
        ordering = ("-created_at",)

    def __str__(self):
        return "{}".format(self.order_title)


class SupplyOrderItem(models.Model):
    supply_order = models.ForeignKey(
        SupplyOrder,
        verbose_name=_("Supply Order"),
        on_delete=models.CASCADE,
    )
    raw_stock = models.ForeignKey(
        RawStock,
        verbose_name=_("Raw Stock"),
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    quantity = models.DecimalField(
        _("Order Quantity"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
        default=Decimal(1),
    )
    actual_quantity = models.DecimalField(
        _("Fulfilled Order Quantity"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
        default=Decimal(0),
    )
    total_cost = models.DecimalField(
        _("Total Cost Price"),
        null=True,
        blank=True,
        decimal_places=2,
        max_digits=10,
    )
    created_at = models.DateTimeField(_("Created Data"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("updated Data"), auto_now=True, editable=False)

    class Meta:
        verbose_name = _("Supply Order Item")
        verbose_name_plural = _("Supply Order Items")
        db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
        ordering = ("-created_at",)

    def __str__(self):
        return "{}".format(self.raw.name)


# class Budget(models.Model):
#     product_order = models.ForeignKey(
#         ProductOrder,
#         verbose_name=_("Product Order"),
#         null=True,
#         blank=True,
#         on_delete=models.CASCADE,
#     )
#     raw_order = models.ForeignKey(
#         RawOrder,
#         verbose_name=_("Raw Material Order"),
#         null=True,
#         blank=True,
#         on_delete=models.CASCADE,
#     )
#     total_income = models.DecimalField(
#         _("Total Revenue"),
#         null=True,
#         blank=True,
#         decimal_places=2,
#         max_digits=10,
#         default=Decimal(0),
#     )
#     total_outcome = models.DecimalField(
#         _("Total Expense"),
#         null=True,
#         blank=True,
#         decimal_places=2,
#         max_digits=10,
#         default=Decimal(0),
#     )
#     salaries = models.DecimalField(
#         _("Salaries"),
#         null=True,
#         blank=True,
#         decimal_places=2,
#         max_digits=10,
#         default=Decimal(0),
#     )
#     total = models.DecimalField(
#         _("Overall Total"),
#         null=True,
#         blank=True,
#         decimal_places=2,
#         max_digits=10,
#         default=Decimal(0),
#     )
#     created_at = models.DateTimeField(_("Created Data"), auto_now_add=True, editable=False)
#     updated_at = models.DateTimeField(_("Updated Data"), auto_now=True, editable=False)

#     class Meta:
#         verbose_name = _("Income/Expense")
#         verbose_name_plural = _("Income/Expense")
#         db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
#         ordering = ("-created_at",)

#     def __str__(self):
#         return "{}".format(self.total)


# class DamagedRaw(models.Model):
#     raw_order = models.ForeignKey(RawOrder, on_delete=models.CASCADE, verbose_name=_("Raw Material Order"))
#     raw = models.ForeignKey(Raw, on_delete=models.CASCADE, verbose_name=_("Raw Material"))
#     created_at = models.DateTimeField(_("Created Data"), auto_now_add=True, editable=False)
#     updated_at = models.DateTimeField(_("Updated Data"), auto_now=True, editable=False)

#     class Meta:
#         verbose_name = _("Damaged Raw Material")
#         verbose_name_plural = _("Damaged Raw Materials")
#         db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
#         ordering = ("-created_at",)

#     def __str__(self):
#         return "{}".format(self.raw.name)


# class DamagedProduct(models.Model):
#     product_order = models.ForeignKey(ProductOrder, on_delete=models.CASCADE, verbose_name=_("Product Order"))
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
#     created_at = models.DateTimeField(_("Created Data"), auto_now_add=True, editable=False)
#     updated_at = models.DateTimeField(_("Updated Data"), auto_now=True, editable=False)

#     class Meta:
#         verbose_name = _("Damaged Product")
#         verbose_name_plural = _("Damaged Products")
#         db_table = verbose_name_plural.replace(" ", "_").replace("/", "_")
#         ordering = ("-created_at",)

#     def __str__(self):
#         return "{}".format(self.product.name)
