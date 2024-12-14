from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister
from django.core.paginator import Paginator
from .models import *


# Create your views here.
def cart(request):
    text = 'Корзина'
    text2 = 'Извините, ваша корзина пуста'
    context = {
        'text': text,
        'text2': text2
    }
    return render(request, 'cart.html', context)


def game(request):
    text = 'ИГРЫ'
    games = Game.objects.all()
    context = {
        'text': text,
        'games': games
    }
    return render(request, 'game.html', context)


def platform(request):
    text = 'Главная страница'
    context = {
        'text': text

    }
    return render(request, 'platform.html', context)


# Create your views here.
def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']

            age = form.cleaned_data['age']
            new_users = Buyer.objects.values_list('name', flat=True)
            if username in new_users:
                info['error'] = f"Пользователь {username} уже существует"

            elif repeat_password != password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = "Вы должны быть старше 18"
            else:
                Buyer.objects.create(name=username, age=age, balance=500)
                info['text'] = f'Приветсвуем, {username}!'

        info['form'] = form

    return render(request, 'registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')
        new_users = Buyer.objects.values_list('name', flat=True)
        if username in new_users:
            info['error'] = f"Пользователь {username} уже существует"

        elif repeat_password != password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = "Вы должны быть старше 18"
        else:
            Buyer.objects.create(name=username, age=age, balance=500)
            info['text'] = f'Приветсвуем, {username}!'

    return render(request, 'registration_page.html', info)


def news(request):
    news = News.objects.all().order_by('date')
    paginator = Paginator(news, 3)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)
    return render(request, 'news.html', {"page_object": page_object})
