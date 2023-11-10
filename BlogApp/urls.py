from django.urls import path
from BlogApp import views

app_name = 'BlogApp'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='create_blog'),
    path('blogdetails/<str:slug>', views.blog_details, name='blog_details'),
    path('liked/<pk>',views.like, name='liked_post'),
    path('unliked/<pk>', views.unlike, name='unliked_post'),
    path('myblogs/', views.MyBlogs.as_view(), name='my_blogs'),
    path('edit_blog/<pk>', views.BlogUpdate.as_view(), name='edit_blog'),
]
