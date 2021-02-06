from django.urls import path
from . import views
app_name = 'comment'
urlpatterns = [
    path('microstory/', views.comment_view, name='microstory'), 
]
