from django.shortcuts import render
from .models import Tovar, Order
# Create your views here.

def index(request):
    if 'query' in request.GET:
        q = request.GET['query']
        tovar = Tovar.objects.filter(title__icontains=q)
    else:
        tovar = Tovar.objects.all()
    return render(request, 'main/index.html', {'tovar':tovar})










def order(request, id):
    order = Tovar.objects.get(pk=id)
    return render(request, 'main/order.html', {'order':order})

def saveorder(request):

    order = Tovar.objects.get(pk=request.POST['orderid'])
    orderprice = request.POST['orderprice']
    o = Order()
    o.name = request.POST['username']
    o.phone = request.POST['phone']
    o.email = request.POST['email']
    o.address = request.POST['address']
    o.tovarname = request.POST['tovarname']
    o.tovarid = order
    o.price = orderprice
    o.save()
    #print(request.POST['orderid'])
    return render(request, 'main/saveorder.html', {'saveorder':saveorder})
