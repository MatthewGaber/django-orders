from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

#Tutorial at https://www.youtube.com/watch?v=3aVqWaLjqS4 used for user authentication

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!, you are now able to login.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'users/register.html', {'form': form})
