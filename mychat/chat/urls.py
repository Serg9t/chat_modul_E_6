from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path('', views.front_page, name='frontpage'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),

    path('rooms/', views.rooms, name='rooms'),
    path('rooms/<slug:slug>/', views.room, name='room'),
    path('users/', views.list_of_users, name='users'),
    path('create/', views.CreateNewRom.as_view(), name='create'),
    path('delete/<slug:slug>', views.DeleteRoom.as_view(), name='delete'),
]
