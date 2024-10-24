from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index-dashboard'),
    path('staff/', views.staff, name='staff-dashboard'),
    path('customer/', views.customer, name='customer-dashboard'),
    path('book/', views.book, name='book-dashboard'),

]
