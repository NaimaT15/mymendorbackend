from django.urls import path
from .views import CreateFeedback

urlpatterns = [
    path('', CreateFeedback.as_view()),
    # path('<str:pk>', Bid.as_view())
]