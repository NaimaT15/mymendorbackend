from django.urls import path
# from .views import CreateBid
from .views import BidWinner
from django.conf.urls import include
from django.urls import re_path
from .views import BidInitialization,BidCommpitionInfo,FindByBidID,Bid_list
urlpatterns = [
    path('BidCommpitionInfo', BidCommpitionInfo.as_view()),
    path('BidInitialization',BidInitialization.as_view()),
    path('winner',BidWinner.as_view()),
    path('Bid_list',Bid_list.as_view()),

    
    re_path(r'^BidBYID/(?P<post_id>\w+)$', FindByBidID.as_view(),name='FindByBidID-list'),
    # path('<str:pk>', Bid.as_view())
]