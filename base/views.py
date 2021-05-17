from django.shortcuts import render
from django.http import HttpResponse

def TaskList(request):
    return HttpResponse('To Do list')
