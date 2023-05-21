from django.db import models

class Booking(models.Model):
    name        = models.CharField(max_length=255)
    no_of_quest = models.IntegerField(6)
    bookingDate = models.DateTimeField()  

class MenuItem(models.Model):
    title       = models.CharField(max_length=255)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    inventory   = models.IntegerField(5)
    
    def __str__(self):
        return f'{self.title} : {str(self.price)}'