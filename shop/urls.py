from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('collections/', views.collections, name='collections'),
    path('collections/<slug:category_slug>/', views.subcollections, name='subcollections'),
    path('collections/<slug:category_slug>/<slug:subcategory_slug>/', views.productview, name='product'),
    path('collections/<slug:category_slug>/<slug:subcategory_slug>/<slug:product_slug>/', views.product_details, name="product_details"),
]
