from django.urls import path
from . import views

urlpatterns = [
    path('thanks/', views.get_thankyou, name="thanks"),
    path('demo/', views.get_demo, name="demo"),
    path('subscribe/', views.subscribe, name='subscribe'),

]