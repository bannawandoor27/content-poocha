from django.urls import path
from . import views
urlpatterns = [
    path('',views.admin_home,name='admin_home'),
    path('delete/<int:id>',views.delete_blog,name='delete_blog'),
]