from django.shortcuts import render

# Create your views here.

def search(request):
    return render(request, 'Booksearch.html')

def result(request):
    return render(request, 'result.html')

def result2(request):
    return render(request, 'result2.html')