from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated 

from .models import Booking, MenuItem
from .serializers import BookingSerializer, MenuItemSerializer


def sayHello(request):
    return HttpResponse("Hello World!")


def index(request):
    return render(request, 'index.html', {})


class BookingViewSet(ModelViewSet):

    queryset            = Booking.objects.all()
    serializer_class    = BookingSerializer
    permission_classes  = [IsAuthenticated]

    '''
    def get(self, request):
        booking_items       = Booking.objects.all()
        booking_serializer  = BookingSerializer(booking_items, many=True) 
        return Response(booking_serializer.data) # Return a JSON Objects with all booking entries
    '''


class MenuItemsView(ListCreateAPIView):

    queryset            = MenuItem.objects.all()
    serializer_class    = MenuItemSerializer

    '''
    def post(self, request):

        booking_serializer = MenuSerializer(data=request.data)

        if booking_serializer.is_valid():
            booking_serializer.save()
            return Response( {'status': 'success', 'data': booking_serializer.data} )
    '''
            
class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset            = MenuItem.objects.all()
    serializer_class    = MenuItemSerializer
    