from django.apps import AppConfig
import os


class AppConfigs(AppConfig):
    app_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
    default_auto_field = "django.db.models.BigAutoField"
    name = f"apps.{app_name}"
    icon = "fa-solid fa-boxes-stacked"
    # <i class="fa-solid fa-boxes-stacked"></i>
