from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect

from blog.models import Blog
from home.forms import ContactForm, OrderForm
from home.models import ContactMessage, Aboutus, Chef
from product.models import Category, Product, Order, Comment
from django.core.paginator import (Paginator, PageNotAnInteger, EmptyPage)

def index(request):
    category = Category.objects.all()
    product_slider = Product.objects.all().order_by('id')
    product_latest = Product.objects.all().order_by('-id')[:5]
    product_picked = Product.objects.all().order_by('?')[:5]
    blog_picked = Blog.objects.all().order_by('?')[:5]
    context = {
        'category': category,
        'product_slider': product_slider,
        'product_latest':product_latest,
        'product_picked':product_picked,
        'blog_picked':blog_picked,
    }
    return render(request,'index.html', context)



def product_detail(request, id, slug):
    product = Product.objects.get(pk=id)
    category = Category.objects.all().order_by('id')
    product_latest = Product.objects.all().order_by('id')
    comments = Comment.objects.filter(product_id=id,)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.name = form.cleaned_data['name']
            data.surname = form.cleaned_data['surname']
            data.phone = form.cleaned_data['phone']
            data.amount = form.cleaned_data['amount']
            data.category = form.cleaned_data['category']
            data.food = form.cleaned_data['food']
            data.address = form.cleaned_data['address']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, 'Siz taom zakaz qildingiz. Operator siz bilan boglanadi!')
            return redirect('index')
    form = OrderForm
    context = {
    'product': product,
    'product_latest':product_latest,
    'category':category,
    'form':form,
    'comments':comments
    }
    return render(request, 'product_detail.html', context)


def category_product(request,id, slug):
    category = Category.objects.all()
    product_latest = Product.objects.all().order_by('-id')[:8]
    products = Product.objects.filter(category_id=id)
    paginator = Paginator(products, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'category': category,
        'products': products,
        'product_latest' : product_latest,

    }
    return render(request, 'menu.html', context)


def contactus(request):
    url = request.META.get('HTTP_REFERER')
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.surname = form.cleaned_data['surname']
            data.phone = form.cleaned_data['phone']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Sizning xabaringiz yuborildi! Rahmat")
            return HttpResponseRedirect(url)
    form = ContactForm
    category = Category.objects.all()
    context = {'form': form,
               'category':category,}
    return render(request,'contact.html', context)

def aboutus(request):
    category = Category.objects.all()
    product_slider = Product.objects.all().order_by('id')
    product_latest = Product.objects.all().order_by('-id')[:8]
    product_picked = Product.objects.all().order_by('?')[:8]
    aboutus = Aboutus.objects.all()
    chef = Chef.objects.all()
    context = {
        'category': category,
        'product_slider': product_slider,
        'product_latest':product_latest,
        'product_picked':product_picked,
        'aboutus':aboutus,
        'chef':chef,
    }
    return render(request,'about_us.html', context)


def chefbio(request,id):
    category = Category.objects.all().order_by('id')
    chef = Chef.objects.get(pk=id)
    product_slider = Product.objects.all().order_by('id')
    context = {
        'chef':chef,
        'product_slider':product_slider,
        'category':category,
    }
    return render(request, 'chefbio.html', context)