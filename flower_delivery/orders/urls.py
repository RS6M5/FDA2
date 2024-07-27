from django.urls import path
from .views import product_list, signup, login_view

urlpatterns = [
    path('', product_list, name='product_list'),
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
]