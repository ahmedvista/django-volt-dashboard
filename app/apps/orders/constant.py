from django.db import models


class ORDER_ITEM_STATUS(models.IntegerChoices):
    PENDING = 0, "PENDING"
    IN_STOCK = 1, "IN SHIPPING"
    SHIPPED = 2, "SHIPPED"
    RETURNED = 3, "RETURNED"
    PARTIALLY_RETURNED = 4, "PARTIALLY RETURNED"

    # SOLD = 4, "SOLD"
    # RETURNED = 5, "RETURNED"
    # IN_MAINTENANCE = 6, "IN MAINTENANCE"
    # DAMAGED = 7, "DAMAGED"


# WAITING = "WAITING"
# FAIL = "FAIL"
# SUCCESS = "SUCCESS"

# PRODUCT_ORDER_STATUS = (
#     (WAITING, "WAITING"),
#     (FAIL, "FAIL"),
#     (SUCCESS, "SUCCESS")
# )

# RAW_ORDER_STATUS = (
#     (WAITING, "WAITING"),
#     (FAIL, "FAIL"),
#     (SUCCESS, "SUCCESS")
# )
