from django.urls import path

from . import views


urlpatterns = [
    path("home/", views.home, name="home"),
    path("products/", views.product_list, name="product_list"),
    path("products/<int:pk>/", views.product_detail, name="product_detail"),
    path("comments/", views.comment_list, name="comment_list"),
]
