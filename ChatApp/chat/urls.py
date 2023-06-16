from django.urls import path
from .views import register_view, login_view, logout_view, chat_view, send_message_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('chat/', chat_view, name='chat'),
    path('send-message/', send_message_view, name='send_message'),
    # Add other URLs as needed
]
