from django.contrib import admin

from .models import PostalCode

@admin.register(PostalCode)
class PostalCodeAdmin(admin.ModelAdmin):
    pass

# Register your models here.
