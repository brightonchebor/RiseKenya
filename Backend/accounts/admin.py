from django.contrib import admin
from .models import User, OneTimePassword

# Register your models here.
# admin.site.register(User)

admin.site.register(OneTimePassword)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_joined', 'last_login']



