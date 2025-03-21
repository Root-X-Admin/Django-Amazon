from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    return render(request, 'healthcare/home.html')

def product_list(request):
    products = Product.objects.all()
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return render(request, 'healthcare/product_list.html', {'products': products, 'form': form})

def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)  # Correct variable name
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)  # Use `product`
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)  # Use `product`
    return render(request, 'healthcare/update_product.html', {'form': form})


def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('product_list')

# Add to Cart (Guest User)
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    # Increase quantity if already in cart
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    return redirect('view_cart')

# View Cart
def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        cart_items.append({'product': product, 'quantity': quantity})

    return render(request, 'healthcare/cart.html', {'cart_items': cart_items})

# Remove from Cart
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        if cart[str(product_id)] > 1:
            cart[str(product_id)] -= 1  # Reduce quantity by 1
        else:
            del cart[str(product_id)]  # Remove item if quantity is 1

    request.session['cart'] = cart
    return redirect('view_cart')

def product_buy(request):
    products = Product.objects.all()
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_buy')
    return render(request, 'healthcare/product_buy.html', {'products': products})