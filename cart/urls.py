from django.urls import path

from . import views

app_name = "cart"
urlpatterns = [
    path('summary/', views.cart_summary, name='cart_summary'),
    path('add/', views.add_to_cart, name='add_to_cart'),
    path('remove/', views.remove_from_cart, name='remove_from_cart'),
    path('update/', views.update_cart_item, name='update_cart_item'),
]
