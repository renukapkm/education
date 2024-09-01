from django.contrib import admin
from .models import Course
from .models import Contacts,Reviews,Registration,Order,Wishlist,Dashregistration




# Register your models here.

admin.site.register(Course)
admin.site.register(Contacts)
admin.site.register(Reviews)
admin.site.register(Registration)
admin.site.register(Order)
admin.site.register(Wishlist)
admin.site.register(Dashregistration)






