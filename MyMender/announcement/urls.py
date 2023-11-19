from django.urls import path
from .views import announce_list,announce
urlpatterns = [
     path('announce_list/',announce_list.as_view()),
     path('',announce.as_view()),
]
