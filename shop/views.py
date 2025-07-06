import json
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, SubCategory, Product, Cart, wishlist_fav
from .form import CustomUserForm 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    products = Product.objects.filter(trending=1)
    return render(request, 'shop/index.html', {"products": products,})

def wishlist_page(request):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.loads(request.body)
            product_id = int(data['pid'])
            product_status = Product.objects.get(id=product_id)

            if product_status:
                if wishlist_fav.objects.filter(user=request.user, product=product_status).exists():
                    return JsonResponse({"status": "Product already in Wishlist"}, status=200)
                else:
                    wishlist_fav.objects.create(user=request.user, product=product_status)
                    return JsonResponse({"status": "Product added to Wishlist"}, status=200)
        else:
            return JsonResponse({"status": "Login to continue"}, status=401)

    elif request.method == "GET":
        if request.user.is_authenticated:
            wishlist_items = wishlist_fav.objects.filter(user=request.user)
            return render(request, "shop/wishlist.html", {"wishlist_items": wishlist_items})
        else:
            return redirect('/login')

    return JsonResponse({"status": "Invalid request"}, status=400)

           
def wishlistview(request):
    if request.user.is_authenticated:
        wishlist_items = wishlist_fav.objects.filter(user=request.user)
        return render(request, 'shop/wishlist.html', {"wishlist_items": wishlist_items})
    else:
        return redirect('/login')

def cart_page(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        return render(request, 'shop/cart.html', {
            "cart_items": cart_items
        })
    else:
        return redirect('/login')

        

def add_to_cart(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.loads(request.body) 
            product_qty = int(data['product_qty'])
            product_id = int(data['pid'])

            product_status = Product.objects.get(id=product_id)

            if product_status:
                if Cart.objects.filter(user=request.user, product=product_status).exists():
                    return JsonResponse({"status": "Product already in cart"}, status=200)
                else:
                    if product_status.quantity >= product_qty:
                        Cart.objects.create(user=request.user, product=product_status, product_qty=product_qty)
                        return JsonResponse({"status": "Product added to cart"}, status=200)
                    else:
                        return JsonResponse({"status": "Product quantity is not available"}, status=200)
        else:
            return JsonResponse({"status": "Login to continue"}, status=401)
    return JsonResponse({"status": "Invalid request"}, status=400)


def remove_cart(request, cart_item_id):
    cartitem=Cart.objects.get(id=cart_item_id)
    cartitem.delete()
    return redirect('/cart')

def remove_wishlist(request, wishlist_item_id):
    wishlistitem=wishlist_fav.objects.get(id=wishlist_item_id)
    wishlistitem.delete()
    return redirect('/wishlist')



def logout_page(request):
    if request.user.is_authenticated:
     logout(request)
     messages.success(request, "You have been logged out successfully.")
    return redirect('/login')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        return render(request, 'shop/login.html')


def register(request):
    form=CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('/login')
    return render(request, 'shop/register.html', {"form": form})

# ✅ All active Categories
def collections(request):
    category = Category.objects.filter(status=0)
    return render(request, 'shop/collections.html', {
        "category": category,
        "category_name": "Collections"
    })

# ✅ All Subcategories under a Category
def subcollections(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = SubCategory.objects.filter(category=category)
    return render(request, "shop/subcollections.html", {
        "subcategory": subcategory,
        "category_name": category.name,
        'category_slug': category.slug,
    })

# ✅ All Products under a Subcategory
def productview(request, category_slug, subcategory_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(SubCategory, slug=subcategory_slug, category=category)
    products = Product.objects.filter(subcategory=subcategory, status=0)
    return render(request, "shop/products/index.html", {
        "products": products,
        "subcategory_name": subcategory.name,
        "subcategory_slug": subcategory.slug,
        "category_name": category.name,
        "category_slug": category.slug
    })

# ✅ Single Product Details Page
def product_details(request, category_slug, subcategory_slug, product_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(SubCategory, slug=subcategory_slug, category=category)
    product = get_object_or_404(Product, slug=product_slug, subcategory=subcategory)
    return render(request, "shop/products/product_details.html", {
        "product": product,
        "product_name": product.name,
        "subcategory_name": subcategory.name,
        "subcategory_slug": subcategory.slug,
        "category_name": category.name,
        "category_slug": category.slug
    })
