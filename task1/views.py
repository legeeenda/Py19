from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import ContactForm


users: list = [
    {'username': 'One', 'password': hash('11111111'), 'age': 22},
    {'username': 'Two', 'password': hash('22222222'), 'age': 22},
]


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


    if any(user['username'] == username for user in users):
        return render_registration_page(request, 'Пользователь уже существует', form)


    new_user: dict = {'username': username, 'password': hash(password), 'age': age}
    users.append(new_user)

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
