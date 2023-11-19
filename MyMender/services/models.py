from django.db import models
from Auth import models as auth_model

# Create your models here.
class services(models.Model):
    ID= models.AutoField(primary_key=True)
    name=models.CharField(max_length=500, null=True)
    dep_ID = models.ForeignKey(auth_model.department, on_delete=models.CASCADE)
    # admin_ID=models.ManyToManyField(auth_model.admin)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.name)
    
class general_requirment(models.Model):
    ID= models.AutoField(primary_key=True)
    description=models.CharField(max_length=1000, null=True)
    #admin_ID = models.ForeignKey(auth_model.admin, on_delete=models.CASCADE)
    service_ID = models.ForeignKey("services", on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.description)
    
# class admin_services(models.Model):
#     ID= models.AutoField(primary_key=True)
#     admin_ID = models.ForeignKey(auth_model.admin, on_delete=models.CASCADE)
#     service_ID = models.ForeignKey("services", on_delete=models.CASCADE)
#     date_created=models.DateTimeField(auto_now_add=True, null=True)
#     def __str__(self):
#         return str(self.ID)
