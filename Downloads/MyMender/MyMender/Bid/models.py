from django.db import models
from django.conf import settings
#from .models import BidInfo
# Create your models here.
...
class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.FloatField()
    bidInfo_id = models.ForeignKey("BidInfo", null=True, on_delete=models.CASCADE)
    numberOfExperience=models.IntegerField()

    # customer_id = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name="pcreator",
    # )
    
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=200, blank=True)
class BidInfo(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=39)
    description = models.TextField(max_length=200)
    initial_price = models.FloatField()
    end_time =models.DateTimeField()
    start_time=models.DateTimeField()
    winner=models.TextField(max_length=20)
    final_price=models.FloatField()
    numberOfExperience=models.IntegerField()
    
    # department_id=models.BigIntegerField()
    
class BidCatagory(models.Model):
    id = models.AutoField(primary_key=True)
    catagoryName=models.TextField(max_length=200)
    

    
    
    

    
    
    
