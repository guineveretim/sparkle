
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import  UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import Group
from django.http import HttpResponse
from .models import Booking
from django.shortcuts import get_object_or_404



def home(request):
  return render(request, 'application/home.html')

def Service(request):
    return render(request, 'application/services.html')


def contact(request):
    return render(request, 'application/contact.html')

def about_view(request):
    return render(request, 'application/about.html')

def bookin(request):
    return render(request, 'application/bookin.html')





def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  
            user.save()
             
            group =Group.objects.get(name = 'user') 
            user.groups.add(group)
            

            login(request, user)  
            messages.success(request, "Registration successful.")
            return redirect('login')  
    else:
        form = UserRegistrationForm()

    return render(request, 'authentication/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
            
                if user.groups.filter(name='admin').exists():
                    login(request, user)
                    return redirect('/admin/')
                elif user.groups.filter(name='user').exists():
                    login(request, user)
                    return redirect('create_booking')
            else:
                
                messages.error(request, 'Invalid username or password.')
        else:
            # Optional: Handle field errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, error)

    else:
        form = UserLoginForm()

    return render(request, 'authentication/login.html', {'form': form})


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Associate the booking with the logged-in user
            booking.save()  # Save the booking record

            # Redirect to the success page with the booking ID
            return redirect('booking_success', booking_id=booking.id) 
    else:
        form = BookingForm()
        
    return render(request, 'accounts/booking.html', {'form': form})



@login_required
def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    context = {
        'service_type': booking.get_service_selection_display(),  # To show a human-readable name for service_selection
        'booking_date': booking.date_time.date(),
        'booking_time': booking.date_time.time(),
        'contact_info': booking.contact_infor,
        'location_info': booking.location_infor,
        'additional_details': booking.additional_details,
    }
    
    return render(request, 'application/bookin.html', context)


             