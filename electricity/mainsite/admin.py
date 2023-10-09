from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from mainsite.models import *


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'surname',
        'name',
        'patronymic',
        'phone'
    )
    list_display_links = (
        'id',
    )
    search_fields = (
        'surname',
        'name',
        'phone'
    )


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'number',
        'date_of_issue',
        'status',
        'slug'
    )
    list_display_links = (
        'id',
        'number'
    )
    search_fields = (
        'number',
    )
    list_filter = (
        'number',
        'date_of_issue',
        'status'
    )
    prepopulated_fields = {
        'slug': (
            'number',
        )
    }


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'address',
        'status',
        'slug'
    )
    list_display_links = (
        'id',
        'name'
    )
    search_fields = (
        'name',
        'address'
    )
    list_filter = (
        'status',
    )
    prepopulated_fields = {
        'slug': (
            'name',
        )
    }


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name'
    )
    list_display_links = (
        'id',
        'name'
    )



@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'code',
        'address',
        'node',
        'contract',
        'start_value',
        'final_value',
        'type',
        'agent',
        'status'
    )
    list_display_links = (
        'id',
        'code'
    )
    search_fields = (
        'code',
        'type__name',
        'address',
        'node__name',
        'start_value',
        'final_value',
        'contract__number',
        'agent__surname'
    )
    list_filter = (
        'node',
        'type',
        'contract',
        'status',
        'agent'
    )
    fieldsets = (
        (' ',
         {
             'fields': (
                 ('code', 'type'),
                 ('address', 'node')
             )
         }
         ),
        (
            'Показания',
            {
                'fields': (
                    ('start_value', 'final_value'),
                )
            }
        ),
        (' ',
         {
             'fields': (
                 'contract',
                 'info',
                 'status',
                 'log',
                 'agent',
             )
         }
         )
    )


@admin.register(ObjectHistory)
class ObjectHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'code',
        'address',
        'node',
        'contract',
        'start_value',
        'final_value',
        'type',
        'agent',
        'status',
        'month',
        'year'
    )
    list_display_links = (
        'id',
        'code'
    )
    search_fields = (
        'code',
        'type__name',
        'address',
        'node__name',
        'start_value',
        'final_value',
        'contract__number',
        'agent__surname',
        'month',
        'year'
    )
    list_filter = (
        'node',
        'type',
        'contract',
        'status',
        'agent',
        'month',
        'year'
    )
    fieldsets = (
        (' ',
         {
             'fields': (
                 ('code', 'type'),
                 ('address', 'node')
             )
         }
         ),
        ('Показания',
         {
             'fields': (
                 (
                    'start_value',
                    'final_value'
                 ),
             )
         }
         ),
        (' ',
         {
             'fields': (
                 'contract',
                 'info',
                 'status',
                 'log',
                 'agent'
             )
         }
         ),
        ('Дата снятия показаний',
         {
             'fields': (
                 ('month', 'year'),
             )
         }
         )
    )


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("last_name", "first_name", "patronymic", "email", "job_title")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
