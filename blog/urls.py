from django.urls import path
from . import views

urlpatterns=[
    path('',views.get_post_blogs,name='get_post_blogs'),
    path('<int:pk>',views.get_update_delete_blog,name='get_update_delete_blog'),
]
