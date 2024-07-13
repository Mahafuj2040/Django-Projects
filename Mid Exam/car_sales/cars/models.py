from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Brand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.name} on {self.car.title}'
    
    

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)


    
    