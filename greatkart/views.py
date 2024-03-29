from django.shortcuts import render
from store.models import Product
from store.models import ReviewRating

def home(request):
    products = Product.objects.all().filter(is_available = True).order_by('created_date')
    for product in products:
        #Get the reviews.
        reviews = ReviewRating.objects.filter(product_id = product.id, status = True)
    context  = {
        'product' : products,
        'reviews' : reviews,
    }
    return render(request, 'home.html', context)