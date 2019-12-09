from django.urls import path
from .import views

app_name = 'a'

urlpatterns = [
	path('', views.home, name = 'home'),
	path('contact/', views.contacts, name = 'contacts'),
	path('(^?P<name>[\w-]+)/', views.car_detail, name = "detail"),
	path('category/(^?P<category_name>[\w-]+)/', views.list_cars_by_category, name = "list_cars_by_category"),
	path('service/', views.service, name = "service")
]
