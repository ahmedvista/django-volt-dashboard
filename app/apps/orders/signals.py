from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save


"""

@receiver(post_save, sender=ProductOrder)
def set_product_order_budget(sender, instance, **kwargs):
    print(instance)
    budget_instance = Budget(product_order=instance)
    budget_instance.save()


@receiver(post_save, sender=RawOrder)
def set_raw_order_budget(sender, instance, **kwargs):
    budget_instance = Budget(raw_order=instance)
    budget_instance.save()


@receiver(pre_save, sender=Budget)
def set_income_total(sender, **kwargs):
    instance = kwargs["instance"]
    if instance.id is None:
        total_income = Budget.objects.all().exclude(product_order__isnull=True).first()

        if total_income is not None:
            if instance.product_order:
                instance.total_income = Decimal(total_income.total_income + instance.product_order.product.unit_price *
                                                instance.product_order.quantity)
        else:
            if instance.product_order:
                instance.total_income = Decimal(instance.product_order.product.unit_price *
                                                instance.product_order.quantity)


@receiver(pre_save, sender=Budget)
def set_outcome_total(sender, **kwargs):
    instance = kwargs["instance"]
    if instance.id is None:
        total_outcome = Budget.objects.all().exclude(raw_order__isnull=True).first()

        if total_outcome is not None:
            if instance.raw_order:
                instance.total_outcome = Decimal(total_outcome.total_outcome - instance.raw_order.raw.unit_price
                                                 * instance.raw_order.quantity)
        else:
            if instance.raw_order:
                instance.total_outcome = Decimal(0 - instance.raw_order.raw.unit_price
                                                 * instance.raw_order.quantity)


@receiver(pre_save, sender=Budget)
def set_budget_total(sender, instance, **kwargs):
    total_outcome = Budget.objects.all().exclude(raw_order__isnull=True).first()
    total_income = Budget.objects.all().exclude(product_order__isnull=True).first()
    instance.total = total_income.total_income + total_outcome.total_outcome
"""


# @receiver(pre_save, sender=ProductOrder)
# def set_product_order_total(sender, instance, **kwargs):
#     instance.total = instance.product.unit_price * instance.quantity

# @receiver(pre_save, sender=RawOrder)
# def set_raw_order_total(sender, instance, **kwargs):
#     instance.total = instance.raw.unit_price * instance.quantity

# @receiver(post_save, sender=RawOrder)
# def set_budget_raw(sender, instance, **kwargs):
#     if instance.status == SUCCESS:
#         budget = Budget.objects.filter()
#         if budget.exists():
#             total = budget.first().total
#         else:
#             total = 0
#         Budget.objects.create(
#             raw_order=instance,
#             total_outcome=instance.total,
#             total=total - instance.total,
#         )

# @receiver(post_save, sender=ProductOrder)
# def set_budget(sender, instance, **kwargs):
#     if instance.status == SUCCESS:
#         budget = Budget.objects.filter()
#         if budget.exists():
#             total = budget.first().total
#         else:
#             total = 0
#         Budget.objects.create(
#             product_order=instance,
#             total_income=instance.total,
#             total=total + instance.total,
#         )

# @receiver(post_save, sender=ProductOrder)
# def add_product_stock(sender, instance, **kwargs):
#     if instance.status == SUCCESS:
#         instance.product.stock.count += instance.quantity
#         instance.product.stock.save()

# @receiver(post_save, sender=ProductOrder)
# def remove_raw_stock(sender, instance, **kwargs):
#     if instance.status == WAITING and kwargs["created"]:
#         raws = instance.product.raws.all()
#         for raw in raws:
#             total = instance.quantity * Decimal(raw.quantity_for_prod)
#             raw.raw.stock.count -= total
#             raw.raw.stock.save()

# @receiver(post_save, sender=RawOrder)
# def add_raw_stock(sender, instance, **kwargs):
# if instance.status == SUCCESS:
#     instance.raw.stock.count += instance.quantity
#     instance.raw.stock.save()


# @receiver(pre_save, sender=Budget)
# def set_budget_for_salaries(sender, instance, **kwargs):
#     if instance.salaries:
#         instance.total -= instance.salaries
