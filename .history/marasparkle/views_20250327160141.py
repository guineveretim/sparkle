
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm
from django.contrib.auth import authenticate, login as auth_login



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
    if request.user.is_authenticated:
        return redirect('home')  # Redirect to home if already logged in
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                next_url = request.GET.get('next', 'home')  # Redirect to 'next' or home
                return redirect(next_url)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Please correct the errors below.")
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



             