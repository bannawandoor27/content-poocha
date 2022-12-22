from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('post_details/<int:id>',views.post_details,name='post_details'),
    path('search',views.search,name='search'),
]