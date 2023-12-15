from django.contrib import admin
from .models import *

# Register your models here.
class ModuleAdmin(admin.ModelAdmin):
    list_display = [
'user',
'brand',
'category',
'File_name',
'text',
'created_at',        
                    ]
class master(admin.ModelAdmin):
    list_display = ["brand","category",            ]
    

admin.site.register(Post, ModuleAdmin)
admin.site.register(masterdata, master)
