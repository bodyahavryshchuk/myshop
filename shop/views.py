from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from cart.forms import CartAddProductForm

from .models import *
from .forms import *


def index(request):
    """Главная страница"""
    num_pr = Product.objects.all().count()

    return render(request, 'ind.html', context={'num_pr': num_pr})


def product_list(request, category_slug=None):
    """Список вмех продуктови по категориям"""
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'store.html', {'category': category, 'categories': categories, 'products': products,
                                          'cart_product_form': cart_product_form})


def product_detail(request, id, slug):
    """Детальная информация продукта"""
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    comments = product.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentCreateForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.product = product
            new_comment.save()
            return redirect('/')
    else:
        comment_form = CommentCreateForm()
    return render(request, 'product.html', {'product': product, 'cart_product_form': cart_product_form,
                                            'comments': comments, 'comment_form': comment_form
                                            })


def categories_list(request):
    """Список категорий"""
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})
