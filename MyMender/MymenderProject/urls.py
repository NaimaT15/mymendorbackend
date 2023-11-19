from django.urls import path,include
from django.contrib import admin

urlpatterns =[
    path('admin/', admin.site.urls),
    path('api/bid/', include('Bid.urls')),
    path('api/feedback/', include('feedback.urls')),
    path('api/announce/', include('announcement.urls')),
    path('api/auth/', include('Auth.urls')),
    path('api/services/', include('services.urls')),
    path('api/app/', include('appointment.urls')),
    path('api/announce/', include('announcement.urls')),
    path('auth/', include('Auth.urls')),
    # path('api/Service/', include('service.urls')),

]







