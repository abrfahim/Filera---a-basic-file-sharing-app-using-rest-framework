from django.contrib import admin

# Register your models here.
from .models import Files, Folder


admin.site.register(Files)
admin.site.register(Folder)