from django.shortcuts import render
from movie_app.models import products
from django.db.models import Q

def SearchResult(request):
    product=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        product=products.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
    return render(request,'search.html',{'query':query,'product':product})
