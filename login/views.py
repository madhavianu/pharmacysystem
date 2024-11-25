from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.cache import cache
import logging
import re

# Create a logger instance
logger = logging.getLogger(__name__)

def is_valid_password(password):
    """Check if the password is valid (at least 6 characters, contains letters and numbers)."""
    return len(password) >= 6 and re.search(r'[A-Za-z]', password) and re.search(r'\d', password)

def admin_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user is blocked
        attempts = cache.get(f'login_attempts_{username}', 0)
        if attempts >= 3:
            return render(request, 'login.html', {'error_message': 'Your account is blocked due to too many failed login attempts.'})

        if not is_valid_password(password):
            return render(request, 'login.html', {'error_message': 'Password must be at least 6 characters long and include letters and numbers.'})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            cache.delete(f'login_attempts_{username}')  # Reset attempts on successful login
            return redirect('admin_dashboard')  # Redirect to the dashboard
        else:
            # Increment the login attempts
            cache.set(f'login_attempts_{username}', attempts + 1, timeout=300)  # Block for 5 minutes
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})

    return render(request, 'login.html')

@login_required
def admin_dashboard(request):
    return render(request, 'home_page.html')  # Homepage view

def admin_logout(request):
    """Logs out the user and redirects them to the login page."""
    logger.info("Logging out user: %s", request.user.username)  # Log the user's name
    logout(request)
    return redirect('admin_login')