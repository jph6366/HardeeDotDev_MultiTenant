from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from Public_HardeeDotDev.models import Client


# TenantAdminMixin is available in order to register the tenant model

# TenantAdminMixin: Mixin for Tenant model
#     It disables save and delete buttons
#     when not in current or public tenant (preventing Exceptions).

@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    # admin.ModelAdmin: Encapsulate all admin options and functionality for a given model.
    list_display = ('name', 'paid_until')
