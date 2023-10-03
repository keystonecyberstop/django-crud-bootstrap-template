from django.urls import path
from .views import index, add, update, delete

urlpatterns = [
    path('', index, name='index'),
    path('add', add, name='add'),
    path('update/<str:id>', update, name='update'),
    path('delete/<str:id>', delete, name='delete'),
]