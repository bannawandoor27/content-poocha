from django.shortcuts import render,redirect
from blog.models import *
# Create your views here.

def admin_home(request):
    all_blogs = BlogData.objects.all().order_by('-created_at')
    context = {
        'all_blogs' : all_blogs
    }
    return render(request,'blog_admin/admin_home.html',context)

def delete_blog(request,id):
    blog = BlogData.objects.get(id=id)
    blog.delete()
    return redirect('admin_home')