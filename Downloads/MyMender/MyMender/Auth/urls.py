from django.urls import path
from .views import user_list, admin_list,dep
urlpatterns = [
     path('user_list/',user_list.as_view()),
     path('admin_list/',admin_list.as_view()),
      path('dep/',dep.as_view()),
]