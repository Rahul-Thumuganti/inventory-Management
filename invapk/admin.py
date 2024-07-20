from django.contrib import admin
from .models import customer,user,Supplier,product,category,Brand,purchase,order

# Register your models here.
admin.site.register(customer)
admin.site.register(user)
admin.site.register(Supplier)
admin.site.register(product)
admin.site.register(category)
admin.site.register(Brand)
admin.site.register(purchase)
admin.site.register(order)

class customeradmin(admin.ModelAdmin):
    list_display = ('id','name','address','mobile_no','balance')  # Include 'status' in list_display
    list_display_links = ('id','name','address','mobile_no','balance')

    search_fields = ('id', 'name')
    ordering = ('name',)


class useradmin(admin.ModelAdmin):
    list_display = ('id','email','password','name','type','status')  # Include 'status' in list_display
    list_display_links = ('id','name')

    search_fields = ('id', 'name','email')
    ordering = ('name',)


class supplieradmin(admin.ModelAdmin):
    list_display = ('id','supplier_name','address','mobile','status')  # Include 'status' in list_display
    list_display_links = ('id','name','address')

    search_fields = ('id', 'name')
    ordering = ('name',)





class productadmin(admin.ModelAdmin):
    list_display = ('id','pname','model','description','Quantity','unit','base_price','tax','minimum_order','supplier','status','date')  # Include 'status' in list_display
    list_display_links = ('id','name')

    search_fields = ('id', 'pname')
    ordering = ('pname',)









class categoryadmin(admin.ModelAdmin):
    list_display = ('id','name',)
    list_display_links = ('id','name')
    search_fields = ('id', 'name')
    ordering = ('pname',)


class brandadmin(admin.ModelAdmin):
    list_display = ('id', 'bname',)



class purchesadmin(admin.ModelAdmin):
    list_display = ('id', 'quantity',)



class orderadmin(admin.ModelAdmin):
    list_display = ('id', 'order_id',)