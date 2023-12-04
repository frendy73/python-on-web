from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def user_detail(request):
    user_id = request.GET.get('id', '')
    user_name = request.GET.get('name', '')
    return HttpResponse(f"Пользователь<br>id: {user_id}, имя: {user_name}")


def index(request):
    return HttpResponse("Index")


def about(request):
    return HttpResponse("About")


def details(request):
    return HttpResponseRedirect('/')
