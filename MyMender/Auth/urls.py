from django.urls import path
from . import views
from knox import views as knox_views
from .views import  admin_dashboard, user_list,dep_list, admin_list,dep,register_user,UserLoginView,UserLogoutView,register_admin
# from knox import views as knox_views
from .views import  admin_dashboard, user_list, admin_list,dep,register_user,UserLoginView,UserLogoutView,register_admin,IsAdmin,IsUser
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
     path('user_list/',user_list.as_view(), name="user_list"),
     #path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
     path('register_user/',register_user.as_view()),
     path('register_admin/',register_admin.as_view()),
     path('adUser_filtermin_list/',admin_list.as_view()),
     path('dep/',dep.as_view(),name="dep"),
     path('dep_list/',dep_list.as_view()),
     
     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
     path('login/', UserLoginView.as_view(),name="login"),
     path('isadmin/', IsAdmin,name="IsAdmin"),
     path('isuser/', IsUser,name="IsUser"),

     # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
     # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
     path('logout/', UserLogoutView.as_view()),
     # path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
     # path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
     path('admin_dashboard/',admin_dashboard.as_view()),


]