from django.urls import path
from .views import AddNotification

urlpatterns = [
    path('', AddNotification.as_view()),
]