from django.shortcuts import render
from chinese.models import Category, Food 
from .models import Cart
# Create your views here.

def customer_index(request):
    # chinese의 모델 내용 사용해야함
    # 즉 다른 앱의 DB를 끌어와야 하는 것
    # 위에서 임포트를 통해 해결
    # 또한 카테고리만 보내면 푸드를 받아올 수 있다.
    category = Category.objects.all()
    context = {
        'category':category
    }
    return render(request, 'customer/index.html', context)

def food_detail(request, pk):
    # object 만들어야함
    food = Food.objects.get(pk=pk)
    context = {
        'object':food
    }
    return render(request, 'customer/customer_detail.html', context)

def add_cart(request):
    # 해당 food_id에 대응되는 데이터의 수량을 add하다 (하나 올려라)
    food_id = request.GET['food_id']
    food = Food.objects.get(pk=food_id)
    # 이전에 해당 음식에 대한 장바구니 정보가 있으면 get
    # 없으면 새로 생성해서 적용
    try:
        cart = Cart.objects.get(food=food)
    except:
        cart = Cart.objects.create(food=food)
    finally:
        pass
    cart.amount += 1
    cart.save()
    context = {
        'object':food
    }
    return render(request, 'customer/customer_detail.html', context)
    
def remove_cart(request):  
    food_id = request.GET['food_id']
    food = Food.objects.get(pk=food_id)
    cart, created = Cart.objects.get_or_create(food=food) # 새롭게 생성되었으면 created = True, 아니면 False 
    if cart.amount > 0:

        cart.amount -= 1
    else:
        cart.amount = 0

    cart.save()
    context = {
        'object':food
    }
    return render(request, 'customer/customer_detail.html', context)

from django.http import JsonResponse
def modify_cart(request):
    # 어떤 음식(food_id)에 amount를 amountChange만큼 변경하고
    # 변경된 최종 결과를 반환(JSON)
    food_id = request.POST['foodId']
    food = Food.objects.get(pk=food_id)
    cart, created = Cart.objects.get_or_create(food=food)
    cart.amount += int(request.POST['amountChange'])
    if cart.amount > 0:
        cart.save()
    
    context = {
        'newQuantity': cart.amount,
        'message':'수량이 성공적으로 업데이트 되었습니다.',
        'success':True
    }
    return JsonResponse(context)