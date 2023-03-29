from django.urls import path
from . import views

urlpatterns=[
    path('',views.index, name='scrape-index'),
    #path('corey/', views.scrape, name='scrape')
]