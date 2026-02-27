from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User



class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email','is_active','is_superuser')
    list_filter = ('email','is_active','is_superuser')
    search_fields = ('email',)
    ordering = ('email',)
    fieldsets = (
        ('Authentication', 
            {'fields':
                ('email', 'password')
            }
        ),

        ('Permissions',
            {'fields':
                ('is_active', 'is_staff', 'is_superuser')
            }
        ),

        ('Group permissions',
            {'fields':
                ('groups', 'user_permissions')
            }
        ),

        ('Important dates',
            {'fields':
                ('last_login',)
            }
        ),

        ('Information',
            {'fields':
                ('name',)
            }
        ),
    
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1','password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )

admin.site.register(User, CustomUserAdmin)