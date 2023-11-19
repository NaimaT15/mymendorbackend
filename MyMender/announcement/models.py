from django.db import models
from Auth import models as auth_model

# Create your models here.
class announcement(models.Model):
    ID= models.AutoField(primary_key=True)
    title=models.CharField(max_length=500, null=True)
    dep_ID = models.ForeignKey(auth_model.department, on_delete=models.CASCADE)
    # admin_ID= models.ForeignKey(auth_model.admin, on_delete=models.CASCADE)
    # admin_ID=models.BigIntegerField(unique=True,)
    description=models.CharField(max_length=5000, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.title)

