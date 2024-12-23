from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Buyer, Game
from .forms import ContactForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from task1.models import Game 

def get_all_games():
    """Получить все игры."""
    return Game.objects.all()

def main(request: HttpRequest) -> HttpResponse:
    """Главная страница."""
    games = get_all_games()
    context = {
        'title': 'Главная страница',
        'games': games,  
    }
    return render(request, 'fourth_task/main.html', context)

def cart(request: HttpRequest) -> HttpResponse:
    """Корзина."""
    games = get_all_games()
    context = {
        'title': 'Корзина',
        'games': games, 
    }
    return render(request, 'fourth_task/cart.html', context)

def shop(request: HttpRequest) -> HttpResponse:
    """Магазин."""
    games = get_all_games()
    context = {
        'title': 'Магазин',
        'games': games,  
    }
    return render(request, 'fourth_task/shop.html', context)



def render_registration_page(request, answer: str, form: ContactForm | None = None) -> HttpResponse:
    """
    Renders the registration page with the given answer and form.
    """
    return render(request, 'fifth_task/registration_page.html', {'answer': answer, 'form': form})

def registration(request: HttpRequest,
                 username: str,
                 password: str,
                 repeat_password: str,
                 age: int,
                 form: ContactForm | None = None) -> HttpResponse:

    if password != repeat_password:
        return render_registration_page(request, 'Пароли не совпадают', form)

    if age < 18:
        return render_registration_page(request, 'Вы должны быть старше 18 лет', form)

    if Buyer.objects.filter(name=username).exists():
        return render_registration_page(request, 'Пользователь уже существует', form)

    Buyer.objects.create(name=username, password_hash=hash(password), age=age)

    return render_registration_page(request, f'Приветствуем {username}!', form)

def sign_up_by_html(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        return registration(request, username, password, repeat_password, age)

    return render_registration_page(request, 'Регистрация')

def sign_up_by_django(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():  
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            return registration(request, username, password, repeat_password, age, form)

    else:
        form = ContactForm()

    return render_registration_page(request, 'Регистрация', form)

def game_list_view(request: HttpRequest) -> HttpResponse:
    games = Game.objects.all()
    return render(request, 'fifth_task/game_list.html', {'games': games})
