from django.shortcuts import render
from django.http import JsonResponse

def test_view(request):
    data ={
        'name':'glen',
        'age':23
    }
    return JsonResponse(data)
