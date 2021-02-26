from django.shortcuts import render
from .models import food
# Create your views here.
def index(request):
    food1=food()
    food1.img=''
    food1.title='Vegetable salad'
    food1.desc='Very Very Very Very Very Very Very Very Very Very Very Very Very Very Very good'
    food1.price=6
    return render(request,'index.html',{'food':food1})