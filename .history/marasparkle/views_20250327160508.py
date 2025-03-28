
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import RegisterForm, LoginForm
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
       form = RegisterForm(request.POST)
       if form.is_valid():
           user = form.save()
           login(request, user) 
           return redirect('login')  
   else:
       form = RegisterForm()
   return render(request, 'authentication/register.html', {'form': form})

@never_cache  # Prevent caching of login page
@csrf_protect  # Extra CSRF protection
def login_view(request):
    # Redirect authenticated users away from login page
    if request.user.is_authenticated:
        messages.info(request, "You're already logged in.")
        return redirect('bookings')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                
                # Handle 'next' parameter for redirects after login
                next_url = request.POST.get('next') or request.GET.get('next', 'bookings')
                return redirect(next_url)
            else:
                # This else might not be needed as form should catch invalid auth
                messages.error(request, 'Invalid username or password.')
        else:
            # Add form errors to messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = LoginForm(request)
    
    context = {
        'form': form,
        'next': request.GET.get('next', '')  # Pass next parameter to template
    }
    return render(request, 'authentication/login.html', context)



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



             