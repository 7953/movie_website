from django.contrib import admin
from . models import category,products,User
from django.contrib.auth.admin import UserAdmin
admin.site.register(User)


class categoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category,categoryAdmin)

class productAdmin(admin.ModelAdmin):
    list_display = ['name','category_id','actors']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(products,productAdmin)
