from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('new_topic/',views.new_topic,name='new_topic'),
    #path('entry/',views.entry, name='entry'),
    path('topic/<int:id>/',views.topic,name='topic'),
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry' ),
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry' ),
] 