from django.shortcuts import render
from .models import Click
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse


def home_page(request, id):
    obj = Click.objects.get(id=id)

    print(obj.users.all())
    print(list(obj.users.all()))

    if User.objects.get(id=int(request.session['_auth_user_id'])) in obj.users.all():
        return render(request, 'game/hello.html', {'data': obj})
    return HttpResponse('<h3>Ошибка доступа</h3>')


def update_clicks(request, id):
    obj = Click.objects.get(id=id)
    obj.click_count += 1
    obj.save()

    return redirect('/{}'.format(id))


def start(request):
    return render(request, 'game/log.html')


def select(request):
    user = authenticate(username=request.POST['user'], password=request.POST['pass'])
    if user:
        login(request, user)
    else:
        return HttpResponse('<h3>Неверный логин или пароль</h3>')

    return redirect('/option')


def click_list(request):
    obj = Click.objects.all().filter(users=request.session['_auth_user_id'])

    return render(request, 'game/your_options.html', {'obj': obj})
