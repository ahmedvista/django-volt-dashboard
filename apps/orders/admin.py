from django.contrib import admin
from django.apps import apps
from django.contrib import admin
import os

app_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
app_models = apps.get_app_config(app_name).get_models()
for model in app_models:
    try:
        admin.site.register(model)

    except Exception:
        pass
