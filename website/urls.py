from django.urls import path
from . import views

urlpatterns = [
    path('thanks/', views.get_thankyou, name="thanks"),
    path('subscribe/', views.get_subscribe, name="subscribe"),
    path('demo/', views.get_demo, name="demo"),
    path('volunteer/', views.get_volunteer, name='volunteeer')
]