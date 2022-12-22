from django.shortcuts import render
from .models import BlogData
# Create your views here.

def home(request):
    all_blogs = BlogData.objects.all().order_by('-created_at')
    context = {
        'blogs' : all_blogs
    }
    return render(request,'home.html',context)


def post_details(request,id):
    post_data = BlogData.objects.get(id=id)
    
    return render(request,'blog/post_details.html',context={'data' : post_data})