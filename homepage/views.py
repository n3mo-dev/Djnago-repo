from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        'Name' : 'jay',
        'DOB' : '02 Oct',
        'Age' : '22',
        'Phone' : 'iphone 12'
    },
    {
        'Name' : 'Jack',
        'DOB' : '10 Oct',
        'Age' : '20',
        'Phone' : 'iphone 11'
    }
]


def homepage(request):
    context = { 'posts' : 'posts'}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')
