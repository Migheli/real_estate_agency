from django.contrib import admin
from django.contrib.auth.models import User
from .models import Flat, Claim, Owner


class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'flat']
    list_display = ['author', 'flat', 'text']


admin.site.register(Claim, ClaimAdmin)


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address',
                    'price',
                    'new_building',
                    'construction_year',
                    'town',
                    'owners_phonenumber',
                    'owner_pure_phone']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['likes']

admin.site.register(Flat, FlatAdmin)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ['owner_name',
                    'owners_phonenumber',
                    'owner_pure_phone',
                    ]

    raw_id_fields = ['flats_of_owner']

admin.site.register(Owner, OwnerAdmin)