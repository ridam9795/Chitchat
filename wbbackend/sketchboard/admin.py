from django.contrib import admin
from .models import User,Chat,Group
# Register your models here.
admin.site.register((User,Chat,Group))
