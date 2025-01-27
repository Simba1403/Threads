from django.urls import path
from. import views

urlpatterns = [
    
    path('',views.thread_list,name='thread_list'),
    path('create/',views.thread_create,name='thread_create'),
    path('<int:thread_id>/edit/',views.edit_thread,name='edit_thread'), #here the int<> is for the thread id
    path('<int:tweet_id>/delete/',views.thread_delete,name='thread_delete'),
    path('register/',views.user_registration,name='user_registration'),
    

    
]
