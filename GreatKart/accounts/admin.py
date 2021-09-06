from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account




# databse e password jate show na hoy se jonno nicher code lekha
class AccountAdmin(UserAdmin):#useradmin ke override korchi
    list_display = ('email','first_name','last_name','username','last_login','date_joined','is_active')
    list_display_links=('email','first_name','last_name')# je field gulote link dorkar 
    readonly_fields=('last_login','date_joined')
    ordering = ('-date_joined',)# eka dhik user thakle descending order e sorte kore dibe
    filter_horizontal=()
    list_filter=()
    fieldsets=()

# Register your models here.
admin.site.register(Account,AccountAdmin)
