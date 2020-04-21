from django.contrib import admin
from .models import Branch
# Register your models here.


class BranchAdmin(admin.ModelAdmin):
    list_display = ('location','manager')


admin.site.register(Branch,BranchAdmin)
