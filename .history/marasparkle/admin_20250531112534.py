from django.contrib import admin
from .models import Booking, ContactUs


class BookingAdmin(admin.ModelAdmin):
  list_display = ('contact_infor','service_selection')
  search_fields= ('contact_infor','service_selection')
  
admin.site.register(Booking, BookingAdmin)

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
  
admin.site.register(ContactUs, ContactUsAdmin)
  