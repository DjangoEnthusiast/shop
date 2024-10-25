from django.contrib import admin
from .models import Member
from .models import Product
from .models import Category
from .models import Cart
from .models import deliverydetails
from .models import savedcard
from .models import order
class web(admin.ModelAdmin):
    list_display=["username"]

class products(admin.ModelAdmin):
    list_display=["productname"]

class categories(admin.ModelAdmin):
    list_display=["categoryname"]

class deliverydetail(admin.ModelAdmin):
    list_display=["id"]

class carddetails(admin.ModelAdmin):
    list_display=["card_holder_name"]

class oid(admin.ModelAdmin):
    list_display=["oid"]

# Register your models here.
admin.site.register(Member,web)
admin.site.register(Product,products)
admin.site.register(Category,categories)
admin.site.register(Cart)
admin.site.register(deliverydetails,deliverydetail)
admin.site.register(savedcard,carddetails)
admin.site.register(order,oid)