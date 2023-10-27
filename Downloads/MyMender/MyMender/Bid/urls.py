from django.urls import path
from .views import CreateBid
from .views import BidInitialization
urlpatterns = [
    path('', CreateBid.as_view()),
    path('',BidInitialization.as_view()),
    
    # path('<str:pk>', Bid.as_view())
]