from django.urls import path
from . import views as views_signup

urlpatterns=[
    path('',views_signup.signup, name='signup')
    
]
