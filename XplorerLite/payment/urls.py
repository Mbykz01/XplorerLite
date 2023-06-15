from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.payment, name='payment'),
    path('success/', views.success_view, name='success'),  # URL mapping for the success page
]