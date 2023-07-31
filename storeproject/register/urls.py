from django.urls import path

from register import views


urlpatterns = [

    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('fill',views.fill,name='fill'),
    path('course', views.course, name='course'),
    path('<int:pk>/',views.fillupdate,name='fillupdate'),
    path('newpage',views.newpage,name='newpage'),


]