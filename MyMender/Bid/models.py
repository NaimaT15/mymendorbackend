from django.db import models
from django.conf import settings
class BidCatagory(models.Model):
    id = models.AutoField(primary_key=True)
    catagoryName=models.TextField(max_length=200)
    status=models.BooleanField()
class Commpetition(models.Model):
    id = models.AutoField(primary_key=True)
    bid_id = models.ForeignKey("Bid",to_field='id', on_delete=models.CASCADE,null=True)
    title = models.TextField(max_length=200, blank=True)
    final_price = models.FloatField()
    winner = models.TextField(max_length=20)
class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=200, blank=True)
    description = models.TextField(max_length=200,null=True)
    catagory_id = models.ForeignKey("BidCatagory",to_field='id', null=True, on_delete=models.CASCADE)
    initial_price = models.FloatField()
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    # minimum_numberOfExperience=models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)


    
    
    
