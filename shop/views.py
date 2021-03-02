from django.shortcuts import render
from .models import food
# Create your views here.
def index(request):

    food1=food()
    food1.img='01.jpg'
    food1.title='Vegetable salad'
    food1.desc='Very Very Very Very Very Very Very Very Very Very Very Very Very Very Very good'
    food1.price='$6'
    # food_list.append(food1)
    food2 = food()
    food2.img = '02.jpg'
    food2.title = 'Aliquam sagittis'
    food2.desc = 'Nam in suscipit nisi, sit amet consectetur metus. Ut sit amet tellus accumsan'
    food2.price = '65'
    # food_list.append(food2)
    food3 = food()
    food3.img = '03.jpg'
    food3.title = 'Sed varius turpis'
    food3.desc = 'Nam in suscipit nisi, sit amet consectetur metus. Ut sit amet tellus accumsan'
    food3.price = '30.50'
    food_list = [food1,food2,food3]
    # food_list.append(food3)
    print(type(food_list))
    print(food_list[0].title)
    print(len(food_list))

    return render(request,'index.html',{'food':food_list})