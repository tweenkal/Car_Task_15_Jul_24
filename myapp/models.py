from django.db import models

# Create your models here.

availablel=[
    ('1','sell'),
    ('2','rent'),
]

bookingl=[
    ('1','confirmed'),
    ('2','cancelled'),
]
class category(models.Model):
    c_name=models.CharField(max_length=30)

    def __str__(self):
        return self.c_name
class brand(models.Model):
    b_name=models.CharField(max_length=30)

    def __str__(self):
        return self.b_name
class city(models.Model):
    city_name=models.CharField(max_length=30)

    def __str__(self):
        return self.city_name
class area(models.Model):
    a_name=models.CharField(max_length=30)
    city_id=models.ForeignKey(city,on_delete=models.CASCADE)

    def __str__(self):
        return self.a_name
class user(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone_no=models.BigIntegerField()
    password=models.CharField(max_length=30)
    add=models.TextField()
    city_id=models.ForeignKey(city,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class car_details(models.Model):
    b_id=models.ForeignKey(brand,on_delete=models.CASCADE)
    m_name=models.CharField(max_length=30)
    year=models.CharField(max_length=30)
    mileage=models.CharField(max_length=30)
    price=models.IntegerField()
    desc=models.TextField()
    available=models.CharField(max_length=30,choices=availablel)

    def __str__(self):
        return self.m_name

class rented_cars(models.Model):
    c_id=models.ForeignKey(car_details,on_delete=models.CASCADE)
    u_id=models.ForeignKey(user,on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()
    total_amount=models.FloatField()
    booking=models.CharField(max_length=30,choices=bookingl)
    a_id=models.ForeignKey(area,on_delete=models.CASCADE)

class sold_car(models.Model):
    c_id=models.ForeignKey(car_details,on_delete=models.CASCADE)
    u_id=models.ForeignKey(user,on_delete=models.CASCADE)
    purchasing=models.DateField()
    selling_amount=models.FloatField()
    a_id=models.ForeignKey(area,on_delete=models.CASCADE)
