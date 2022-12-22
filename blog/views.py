from django.shortcuts import render
from .models import BlogData
from django.db.models import Q
# Create your views here.

def home(request):
    all_blogs = BlogData.objects.all().order_by('-created_at')
    
    context = {
        'blogs' : all_blogs,
    }
    return render(request,'home.html',context)


def post_details(request,id):
    post_data = BlogData.objects.get(id=id)
    
    return render(request,'blog/post_details.html',context={'data' : post_data})

def search(request):
    if request.method == 'GET':
        search_key = request.GET['search_key']
        if search_key:
            search_result = BlogData.objects.order_by('-created_at').filter(Q(heading__icontains=search_key)|Q(description__icontains=search_key)|Q(category__icontains=search_key))
    else:
        pass
    context = {
        'results':search_result
    }
    return render(request,'home.html',context)