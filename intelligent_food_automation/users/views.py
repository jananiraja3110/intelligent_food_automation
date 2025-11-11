from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Auto-approve admin users, others need approval
            if user.role == 'admin':
                user.is_approved = True
            user.save()
            messages.success(request, 'Registration successful! Please wait for admin approval.')
            return redirect('users:login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                # Allow login if: approved OR admin role OR superuser
                if user.is_approved or user.role == 'admin' or user.is_superuser:
                    login(request, user)
                    messages.success(request, f'Welcome back, {username}!')
                    return redirect('core:dashboard')
                else:
                    messages.error(request, 'Your account is pending approval. Please contact administrator.')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})

def custom_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('core:home')

@login_required
def profile(request):
    return render(request, 'users/profile.html', {'user': request.user})