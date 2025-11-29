from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from shop.models import Product
from shop.models import Product  # keep as needed
from shop import models as shop_models
from shop.models import Product
from cart.models import CartItem   # type: ignore # your cart app model (I saw cart.html earlier)
from .models import ShippingAddress, Order, OrderItem, Payment

@login_required
def checkout_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        address = ShippingAddress.objects.create(
            user=request.user,
            address=request.POST['address'],
            city=request.POST['city'],
            state=request.POST['state'],
            zipcode=request.POST['zipcode'],
            phone=request.POST['phone'],
        )

        order = Order.objects.create(
            user=request.user,
            address=address,
            total_price=total_price
        )

        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)

        return redirect('payment', order_id=order.id)

    return render(request, 'orders/checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })


@login_required
def payment_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)

    if request.method == 'POST':
        mode = request.POST.get('payment_mode')
        payment = Payment.objects.create(order=order, payment_mode=mode, payment_status='Completed' if mode != 'Cash on Delivery' else 'Pending')
        order.status = 'Confirmed'
        order.save()

        # clear cart after order is created & payment confirmed (for COD we still clear)
        CartItem.objects.filter(user=request.user).delete()

        return redirect('order_success', order_id=order.id)

    return render(request, 'orders/payment.html', {'order': order})


@login_required
def order_success_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_success.html', {'order': order})


@login_required
def my_orders_view(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/my_orders.html', {'orders': orders})
