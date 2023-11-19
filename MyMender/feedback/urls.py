from django.urls import path
from .views import CreateFeedback,FeedBack_list

urlpatterns = [
    path('', CreateFeedback.as_view()),
    path('view', FeedBack_list.as_view()),

    
    # path('<str:pk>', Bid.as_view())
]