from django.urls import path
from .views import announce_list
urlpatterns = [
     path('list/',announce_list.as_view()),
]
