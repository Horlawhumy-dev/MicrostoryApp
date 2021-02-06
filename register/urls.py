from django.urls import path
from . import views 

app_name = 'register'
urlpatterns = [
    path('', views.base_view, name='base'),
    path('signup/',views.register_view, name='signup'),
    path('signin/',views.signin_view, name='signin'),
    path('signout/',views.signout_view, name='signout')
]
