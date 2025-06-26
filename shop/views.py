from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, SubCategory, Product
from .form import CustomUserForm 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def home(request):
    products = Product.objects.filter(trending=1)
    return render(request, 'shop/index.html', {"products": products,})

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
