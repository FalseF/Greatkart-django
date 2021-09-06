from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):#slug field e auto medic category name save korar jonno ei code
    prepopulated_fields={'slug':('category_name',)}
    list_display = ('category_name','slug')
admin.site.register(Category,CategoryAdmin)
