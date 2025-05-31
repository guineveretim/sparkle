from django.db import models
from django.contrib.auth.models import User



class Booking (models.Model):
   
  SERVICE_CHOICES=[
    ('home_cleaning', 'Home_cleaning'),
    ('office_cleaning', 'Office_cleaning'),
    ('maintanance', 'Maintanance'),
    ('maid_placement', 'Maid_Placement'),
    
  ]
   
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
  date_time =models.DateTimeField(null=True, auto_now=False, auto_now_add=False)
  contact_infor = models.CharField(max_length=15,blank=False)
  service_selection = models.CharField(max_length=20,choices=SERVICE_CHOICES,default='home_cleaning')
  location_infor= models.CharField(max_length=100, blank=False)
  additional_details = models.CharField(max_length=150, blank=True)
  
  def __str__(self):
        return f"{self.contact_infor} - {self.service_selection}"
      
class ContactUs(models.Model):
      name = models.CharField(max_length=100)
      email = models.EmailField()
      message = models.TextField()
  
      def __str__(self):
          return f"{self.name} - {self.email}"