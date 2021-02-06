from django.urls import path
from . import views

app_name = "results_app"
urlpatterns = [
    path('results/', views.results_view, name='results')
]
