from django.contrib import admin
from .models import Flat, Claim, Owner


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ['author', 'flat']
    list_display = ['author', 'flat', 'text']


class FlatOwnersInline(admin.TabularInline):
    model = Flat.owned_by.through
    raw_id_fields = ['owner']


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner']
    readonly_fields = ['created_at']
    list_display = ['address',
                    'price',
                    'new_building',
                    'construction_year',
                    'town',
                    ]
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['likes']
    inlines = [FlatOwnersInline]


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['owner_name',
                    'owners_phonenumber',
                    'owner_pure_phone',
                    ]
    raw_id_fields = ['flats_of_owner']
