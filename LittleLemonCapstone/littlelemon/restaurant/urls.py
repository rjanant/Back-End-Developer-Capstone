
from django.contrib import admin
from django.urls import path, include
from .views import sayHello, index, MenuItemsView, SingleMenuItemView, BookingViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'tables', BookingViewSet)


urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]