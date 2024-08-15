from django.contrib import admin
from .models import Bank

# Register your models here.
@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('id','acc_no','acc_holder','acc_balance')
