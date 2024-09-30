from django.contrib import admin
from.models import category,brand,city,area,user,car_details,rented_cars,sold_car

# Register your models here.

class showcategory(admin.ModelAdmin):
    list_display = ["c_name"]

admin.site.register(category,showcategory)

class showbrand(admin.ModelAdmin):
    list_display = ["b_name"]

admin.site.register(brand,showbrand)

class showcity(admin.ModelAdmin):
    list_display = ["city_name"]

admin.site.register(city,showcity)

class showarea(admin.ModelAdmin):
    list_display = ["a_name","city_id"]

admin.site.register(area,showarea)

class showuser(admin.ModelAdmin):
    list_display = ["name","email","phone_no","password","add","city_id"]

admin.site.register(user,showuser)

class showcar_details(admin.ModelAdmin):
    list_display = ["b_id","m_name","year","mileage","price","desc","available"]

admin.site.register(car_details,showcar_details)

class showrented_car(admin.ModelAdmin):
    list_display =["c_id","u_id","start_date","end_date","total_amount","booking","a_id"]

admin.site.register(rented_cars,showrented_car)

class showsold_car(admin.ModelAdmin):
    list_display = ["c_id","u_id","purchasing","selling_amount","a_id"]

admin.site.register(sold_car,showsold_car)