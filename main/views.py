from django.shortcuts import render
from .models import BZU
from .models import Fruit

# def GetFruit(request):
#     return render(request, 'layout.html', {'data' : {
#         'fruits': Fruit.objects.all()
#     }})

# def GetBZU(request, id):
#     return render(request, 'book.html', {'data' : {
#         'current_date': date.today(),
#         'book': Book.objects.filter(id=id)[0]
#     }})

# Create your views here.
def index(request):
    return render(request, 'main/index.html')
def carrot(request):
    return render(request, 'main/carrot.html')
def apple(request):
    return render(request, 'main/apple.html')
def papper(request):
    return render(request, 'main/papper.html')
def lemon(request):
    return render(request, 'main/lemon.html')



