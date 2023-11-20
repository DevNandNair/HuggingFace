
from django.urls import path
from .views import summarize



urlpatterns = [
    path('', summarize, name='summarize'),
    
]
