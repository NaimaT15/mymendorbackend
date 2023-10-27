from django.db import models

class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(max_length=200, blank=True)
    # customer_id = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name="customer",
    # )
    # service_id = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.SET_NULL,
    #     null=True,
    #     blank=True,
    #     related_name="service",
    # )    
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.TextField(max_length=20, blank=True)
