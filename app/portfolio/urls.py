from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    # Function View
    # path('details/<int:pk>/', views.post_detail, name='details'),
]
