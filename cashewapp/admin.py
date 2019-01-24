from django.contrib import admin

from .models import *

class TransactionAdmin(admin.ModelAdmin):    
    list_display = ('date', 'category', 'account', 'formatted_amount')
    
class TypeAdmin(admin.ModelAdmin):    
    list_display = ('name', 'table')
    
class AccountAdmin(admin.ModelAdmin):    
    list_display = ('name', 'type', 'currency', 'active')
    
class CategoryAdmin(admin.ModelAdmin):    
    list_display = ('name', 'parent', 'active')    

admin.site.register(Category,CategoryAdmin)
admin.site.register(Type,TypeAdmin)
admin.site.register(Currency)
admin.site.register(Account,AccountAdmin)
admin.site.register(Transaction,TransactionAdmin)
