from .models import CartItem,Cart
from .views import _cart_id

def counter(request):
    cart_count = 0

    if 'admin' in request.path:
        return {}
    else:
        try:
            cart=Cart.objects.filter(cart_id = _cart_id(request))

            cart_items = CartItem.objects.all().filter(cart = cart[:1])
            # here cart[:1] means items theke sudo ekta item nibo 
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
        
        return dict(cart_count = cart_count )


