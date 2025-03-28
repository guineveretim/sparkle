
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BookingForm
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect



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
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'authentication/register.html', {'form': form})


@never_cache  # Prevent caching of login page
@csrf_protect  # Extra CSRF protection
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to a success page
            else:
                form.add_error(None, "Invalid username or password.")  # Handle invalid credentials
    else:
        form = UserLoginForm()
    
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



             