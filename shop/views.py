import requests
from django.http import HttpResponse

def greetings(requests):
    return HttpResponse('Добро пожаловать')

def cats(request):
    response = requests.get('https://catfact.ninja/fact').json()
    print(response)
    return HttpResponse(response['fact'])
