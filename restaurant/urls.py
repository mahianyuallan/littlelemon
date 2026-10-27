from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/', views.sayHello, name='sayHello'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/items/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]
