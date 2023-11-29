from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    ip = request.META['REMOTE_ADDR']

    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>Browser: {user_agent}</p>
        <p>IP: {ip}</p>
    """)

def error(request):
    return HttpResponse ('<h1> К сожалению произошла ошибка </h1>', status=400, reason=('Incorrect data'))




def user(request, name='Undefined', folder='Undefined', post='0'):
    return HttpResponse(f'<h2>Логин: {name}</h2> <br> <h2> Папка с постами называется {folder} <br> Пост номер {post}')


def folder(request, name='Undefined', folder='Undefined', post='0'):
    return HttpResponse(f'<h2>Логин: {name}</h2> <br> <h2> Папка с постами называется {folder}<br> Пост номер {post}')


def post(request, name='Undefined', folder='Undefined', post='0'):
    return HttpResponse(f'<h2>Логин: {name}</h2> <br> <h2> Папка с постами называется {folder} <br> Пост номер {post}')


