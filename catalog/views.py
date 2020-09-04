from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Product
def home(request):
    product = Product.objects
    return render(request, 'home.html',{'product':product})

@login_required(login_url="/signup/")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] :
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            if request.FILES['icon'] and request.FILES['image']:
                product.icon = request.FILES['icon']
                product.image = request.FILES['image']
            else:
                return render(request, 'product.html', {'error': 'files are required'})
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/'+ str(product.id))
        else:
            return render(request, 'product.html', {'error':'all fields required'})
    else:
        return render(request, 'product.html')

def detail(request,product_id):
    proddetails = get_object_or_404(Product,pk=product_id)
    return render(request, 'detail.html', {'proddetails':proddetails})

@login_required(login_url="/signup/")
def upvote(request,product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product,pk=product_id)
        product.vote_count += 1
        product.save()
        return redirect('/'+ str(product.id))