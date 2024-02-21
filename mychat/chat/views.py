from django.contrib.auth.decorators import login_required
from django.contrib.messages import success
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import get_user_model, login
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, CreateView, DeleteView

from .models import User, Room, Message
from .forms import RoomForm, SingUpForm, UserLoginFrom, ProfileUserForm


# Представление для главной/домашней страницы
def front_page(request):
    return render(request, 'chat/frontpage.html')


# Регистрация пользователя
def sign_up(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            
            return redirect('frontpage')
    else:
        form = SingUpForm()
    
    return render(request, 'chat/signup.html', {'form': form})


# Авторизация пользователя
def log_in(request):
    if request.method == 'POST':
        form = UserLoginFrom(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('frontpage'))
    else:
        form = UserLoginFrom()
    
    return render(request, 'chat/login.html', {'form': form})


# Профиль пользователя и возможность редактировать
class ProfileUser(UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'chat/profile.html'
    extra_context = {'title': 'Профиль пользователя'}

    def get_success_url(self):
        return reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user
    

# Отображение всех комнат
@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'chat/rooms.html', {'rooms': rooms})


# Комната для чата/отправки сообщений
@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)

    return render(request, 'chat/room.html', {'room': room, 'messages': messages})


# Отображение списка пользователей
def list_of_users(request):
    users = User.objects.all()

    return render(request, 'chat/users.html', {'users': users})


# Создание комнаты
class CreateNewRom(CreateView):
    form_class = RoomForm
    template_name = 'chat/create_room.html'
    success_url = reverse_lazy('frontpage')


# Удаление комнаты (удалять может только админ)
class DeleteRoom(DeleteView):
    model = Room
    template_name = 'chat/delete_room.html'
    success_url = reverse_lazy('frontpage')
