from django.urls import path

from storeapp import views
app_name='storeapp'
urlpatterns = [

    path('',views.home,name='home'),
]
