from django.contrib import admin
from .models import Staff, Stock, Vehicle, Bookingbycustomer, Bookingbystaff, Customer, VehicleDetails, feedback
# Register your models here.
admin.site.register(Staff)
admin.site.register(Stock)
admin.site.register(Vehicle)
admin.site.register(Bookingbycustomer)
admin.site.register(Bookingbystaff)
admin.site.register(Customer)
admin.site.register(VehicleDetails)
admin.site.register(feedback)
