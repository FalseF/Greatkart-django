from django.core.exceptions import ObjectDoesNotExist
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .import views
from store.models import Product
from category.models import Category
from carts.models import Cart, CartItem
# Create your views here.

#cart id return korbe
def _cart_id(request):#underscore means it is a private function

    cart = request.session.session_key# ekhane product er id dhorchi 
    if not cart:
        cart = request.session.create()# id na thakle new kore id create kore dichi
    return cart


def add_cart(request,product_id):

    product = Product.objects.get(id=product_id)

    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        # Get the cart  using the cart_id present int the session

    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request),
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)# product and cartItem merge korchi 
        #eka dhik product add korle quantity increment korchi
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            cart = cart,
            quantity = 1,
        )

    cart_item.save()
    return redirect ('cart')    

def remove_cart(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item=CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart_item(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product,id=product_id)
    cart_item=CartItem.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('cart')





def cart(request,total = 0, quantity=0, cart_items = None):
    try:
        cart = Cart.objects.get(cart_id = _cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart,is_active=True)
        for item in cart_items :
            total += (item.product.price * item.quantity)
            quantity += item.quantity

        tax = ( 2 * total ) /100
        grand_total = total+ tax
        
    except ObjectDoesNotExist:
        pass

    context={
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax':tax,
        'grand_total':grand_total,

    }

    return render(request,'store/cart.html',context)
 