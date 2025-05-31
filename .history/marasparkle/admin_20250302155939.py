from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
  list_display = ('contact_infor','service_selection')
  search_fields= ('contact_infor','service_selection')
  
admin.site.register(Booking, BookingAdmin)
  