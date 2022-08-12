from django.contrib import admin
from django.urls import path
from userSystem import settings
from django.conf.urls.static import static
from base import views, userViews

urlpatterns = [   
    path('',views.ShowLoginPage,name="show_login"),
    path('doLogin',views.doLogin,name="do_login"),
    path('logout_user', views.logout_user,name="logout"),
    path('teacher_home', userViews.teacher_home, name="teacher_home"),
    path('student_home', userViews.student_home, name="student_home"),
    path('add_request', userViews.add_request, name="add_request"),
    path('add_request_save', userViews.add_request_save, name="add_request_save"),
    path('view_request/<str:request_id>', userViews.view_request,name="view_request"),
    path('accept_request/<str:request_id>', userViews.accept_request,name="accept_request"),
    path('reject_request/<str:request_id>', userViews.reject_request,name="reject_request"),
    path('add_recommendation_letter', userViews.add_recommendation_letter, name="add_recommendation_letter"),
    path('add_recommendation_letter_save', userViews.add_recommendation_letter_save, name="add_recommendation_letter_save"),
    path('view_recommendation_letter', userViews.view_recommendation_letter, name="view_recommendation_letter"),
]
