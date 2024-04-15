from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Food, Category
from django.core.files.storage import FileSystemStorage
# Create your views here.

# def upload(request):
#     fs=FileSystemStorage()
#     uploaded_file = request.FILES['file']
#     name = fs.save(uploaded_file.name, uploaded_file)
#     url = fs.url(name)
#     return HttpResponse("{}에 저장이 잘 되었습니다.".format(url))

def index(request):
    # get(주소만 입력해서 오는 것) -> 페이지만 보여주고
    # post -> DB에 입력하는 과정을 넣자
    if request.method == 'GET':
        return render(request=request, template_name='chinese/index.html')
    
    elif request.method == 'POST':
        category = Category.objects.get(name=request.POST['category'])
        food_name = request.POST['foodname']
        food_price = request.POST['price']
        food_description = request.POST['description']
        food_takeout = request.POST['takeout']

        # 이미지 업로드
        fs = FileSystemStorage()
        uploaded_file = request.FILES['file']
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)

        Food.objects.create(category=category,
                            name=food_name,
                            price=food_price,
                            description=food_description,
                            image_url=url)
        return render(request=request, template_name='chinese/index.html')
    
def food_detail(request, pk):
    object = Food.objects.get(pk=pk)
    context = {
        'object':object
    }
    return render(request=request, template_name='chinese/food_detail.html', context=context)

def food_delete(request, pk):
    object = Food.objects.get(pk=pk)
    object.delete()
    return redirect('http://127.0.0.1:8000/')