from django.contrib import admin

from study_management_app import models

# Register your models here.
admin.site.register(models.Study)
admin.site.register(models.Sponsors)