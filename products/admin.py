from django.contrib import admin
from . models import product,offers,emplo

class productAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')

class emploAdmin(admin.ModelAdmin):
    list_display = ('name','age')    

# Register your models here.
admin.site.register(product,productAdmin)
admin.site.register(offers)
admin.site.register(emplo,emploAdmin)

