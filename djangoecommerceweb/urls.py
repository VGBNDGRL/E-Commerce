from django.urls import path
from . import views

urlpatterns = [
    path("", views.ecommerce_index, name="ecommerce_index"),
    path("<int:pk>/", views.ecommerce_detail, name="ecommerce_detail"),
]