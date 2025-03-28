
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm



def home(request):
  return render(request, 'home.html')

def Service(request):
    return render(request, 'application/services.html')


def contact(request):
    return render(request, 'application/contact.html')

def about_view(request):
    return render(request, 'application/about.html')

  
def register(request):
   if request.method == 'POST':
       form = RegisterForm(request.POST)
       if form.is_valid():
           user = form.save()
           login(request, user) 
           return redirect('login')  
   else:
       form = RegisterForm()
   return render(request, 'authentication/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user) 
                return redirect('bookings') 
            else:
                
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
            
    return render(request,'accounts/booking.html', {'form':form})



             