from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('cart/', views.cart_page, name='cart'),
    path('wishlist/', views.wishlist_page, name='wishlist'),
    path('wishlistview/', views.wishlistview, name='wishlistview'),
    path('remove_wishlist/<slug:wishlist_item_id>/', views.remove_wishlist, name='remove_wishlist'),
    path('remove_cart/<slug:cart_item_id>/', views.remove_cart, name='remove_cart'),
    path('collections/', views.collections, name='collections'),
    path('collections/<slug:category_slug>/', views.subcollections, name='subcollections'),
    path('collections/<slug:category_slug>/<slug:subcategory_slug>/', views.productview, name='product'),
    path('collections/<slug:category_slug>/<slug:subcategory_slug>/<slug:product_slug>/', views.product_details, name="product_details"),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),

]
