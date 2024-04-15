
from django.urls import path, include
from . import views
app_name = "chinese"
urlpatterns = [
    path('', views.index, name='chinese_index'),
    path('food_detail/<int:pk>', views.food_detail, name='food_detail'),
    path('food_delete/<int:pk>', views.food_delete, name='food_delete')
    
]
