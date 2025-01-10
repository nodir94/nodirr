from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Postlar ro'yxati sahifasi
    path('<int:id>/', views.post_detail, name='post_detail'),  # Post tafsilot sahifasi
]
