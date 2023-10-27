from django.db import models
from services import models as service_model
from Auth import models as auth_model

class appointment(models.Model):
    ID= models.AutoField(primary_key=True)
    customer_ID = models.ForeignKey(auth_model.customer, on_delete=models.CASCADE)
    admin_service_ID = models.ForeignKey(service_model.admin_services, on_delete=models.CASCADE)
    dep_ID = models.ForeignKey(auth_model.department, on_delete=models.CASCADE)
    app_date=models.DateField()
    status=models.CharField(max_length=500, null=True)
    date_created=models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return str(self.customer_ID)
    
