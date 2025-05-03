from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

#from .forms import ReviewForm
from .models import Category, Product, Review


def home(request):
    products = Product.objects.all()
    categories = Category.objects.annotate(product_count=Count("products"))

    context = {"products": products, "categories": categories}

    return render(request, "products/home.html", context)


def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    products = Product.objects.filter(category=category)
    paginator = Paginator(products, 6)
    page = request.GET.get("page")
    paged_products = paginator.get_page(page)

    context = {
        "products": paged_products,
        "category": category,
    }
    return render(request, "products/category_products.html", context)


def product_detail(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    #reviews = product.reviews.filter(status=True)

    context = {
        "product": product,
        "rating_counts": rating_counts,
        "rating_percentages": rating_percentages,
        "reviews": reviews,
    }
    return render(request, "products/product-left-thumbnail.html", context)