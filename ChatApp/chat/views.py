from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User, Chat

def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        contact_no = request.POST.get('contact_no')
        # Create a new user object
        user = User.objects.create_user(email=email, password=password, name=name, gender=gender, dob=dob, contact_no=contact_no)
        # Redirect to login page or any other page
        return redirect('login')
    return render(request, 'registration.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to chat screen or any other page
            return redirect('chat')
        else:
            # Show error message for invalid credentials
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    # Redirect to login page or any other page
    return redirect('login')

def chat_view(request):
    users = User.objects.all()
    selected_user_id = request.GET.get('user_id')
    selected_user = User.objects.get(id=selected_user_id) if selected_user_id else None
    chats = Chat.objects.filter(sender=request.user, receiver=selected_user) | Chat.objects.filter(sender=selected_user, receiver=request.user)
    return render(request, 'chat.html', {'users': users, 'selected_user': selected_user, 'chats': chats})

def send_message_view(request):
    if request.method == 'POST':
        receiver_id = request.POST.get('receiver_id')
        message = request.POST.get('message')
        receiver = User.objects.get(id=receiver_id)
        chat = Chat(sender=request.user, receiver=receiver, message=message)
        chat.save()
        # Redirect to chat screen or any other page
        return redirect('chat')
