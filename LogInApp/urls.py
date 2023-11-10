from django.urls import path
from LogInApp import views


app_name = 'LogInApp'

urlpatterns = [
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change-profile/', views.user_change, name='change_profile'),
    path('password/', views.pass_change, name='password'),
    path('addprofilepic/', views.add_profile_pic, name='add_profile_pic'),
    path('change_profile/', views.change_pro_pic, name='change_profile_pic'),
]

