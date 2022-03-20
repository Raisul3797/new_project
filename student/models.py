from django.db import models

# Create your models here.
class customer_info(models.Model):
    customer_id=models.IntegerField()
    customer_name=models.CharField(max_length=20)
    customer_org=models.CharField(max_length=15)
    email=models.CharField(max_length=20)
    NID=models.IntegerField()
    phone=models.CharField(max_length=20)


class room_info(models.Model):
    room_num=models.IntegerField()
    room_name=models.CharField(max_length=10)
    room_size=models.IntegerField()

class Contact(models.Model):
    Name=models.CharField(max_length=100)
    Phone=models.IntegerField()
    Email=models.CharField(max_length=20)
    Comments=models.TextField(max_length=500)
