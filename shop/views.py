from django.shortcuts import render
from .models import food
# Create your views here.
def index(request):
    food_list = []
    food1=food()
    food1.img='01.jpg'
    food1.title='Vegetable salad'
    food1.desc='Very Very Very Very Very Very Very Very Very Very Very Very Very Very Very good'
    food1.price='$6'
    food_list.append(food1)
    food2 = food()
    food2.img = '02.jpg'
    food2.title = 'Aliquam sagittis'
    food2.desc = 'Nam in suscipit nisi, sit amet consectetur metus. Ut sit amet tellus accumsan'
    food2.price = '65'
    food_list.append(food2)
    food3 = food()
    food3.img = '03.jpg'
    food3.title = 'Sed varius turpis'
    food3.desc = 'Nam in suscipit nisi, sit amet consectetur metus. Ut sit amet tellus accumsan'
    food3.price = '30.50'

    # food_list = [food1,food2,food3]
    food_list.append(food3)
    food4 = food()
    food4.img = '04.jpg'
    food4.title = 'Aliquam sagittis'
    food4.desc = 'Nam in suscipit nisi, sit amet consectetur metus. Ut sit amet tellus accumsan'
    food4.price = '$25.50'
    food_list.append(food4)
    food5 = food()
    food5.img = '05.jpg'
    food5.title = 'Maecenas eget justo'
    food5.desc = 'Nam in suscipit nisi, sit amet consectetur metus. Ut sit amet tellus accumsan'
    food5.price = '$80.25'
    food_list.append(food5)
    food6 = food()
    food6.img = '06.jpg'
    food6.title = 'Quisque et felis eros'
    food6.desc = 'Nam in suscipit nisi, sit amet consectetur metus. Ut sit amet tellus accumsan'
    food6.price = '$20 / $40 / $60'
    food_list.append(food6)
    food7 = food()
    food7.img = '07.jpg'
    food7.title = 'Sed ultricies dui'
    food7.desc = 'Nam in suscipit nisi, sit amet consectetur metus. Ut sit amet tellus accumsan'
    food7.price = '$94'
    food_list.append(food7)
    food8 = food()
    food8.img = '08.jpg'
    food8.title = 'Donec porta consequat'
    food8.desc = 'Nam in suscipit nisi, sit amet consectetur metus. Ut sit amet tellus accumsan'
    food8.price = '$15'
    food_list.append(food8)

    print(type(food_list))
    print(food_list[0].title)
    print(len(food_list))

    return render(request,'index.html',{'food':food_list})


