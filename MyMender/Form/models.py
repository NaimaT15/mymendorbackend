from django.db import models

class Form(models.Model):
    id = models.AutoField(primary_key=True)
    department_id= models.ForeignKey('Auth.department',to_field='ID', on_delete=models.CASCADE,null=True)
    field_id= models.ForeignKey('FormField',to_field='id', on_delete=models.CASCADE,null=True)
    service_id= models.ForeignKey('services.services',to_field='ID', on_delete=models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
 
class FormField(models.Model):
    id = models.AutoField(primary_key=True)
    field_name=models.CharField(max_length=500, null=True)
    datatype_id= models.ForeignKey('Datatype',to_field='id', on_delete=models.CASCADE,null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
class Datatype(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=500, null=True)
