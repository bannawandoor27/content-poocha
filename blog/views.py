from django.shortcuts import render,redirect

from .models import BlogData
from django.db.models import Q
from django.core.mail import EmailMessage
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
    if not search_result:
        message = 'Ugh..Its seems like I haven\'t put anything like that yet!'
    else:
        message = ''
    context = {
        'results':search_result,
        'message':message
    }
    return render(request,'home.html',context)

def contact(request):
    return render(request,'blog/contact.html')

def subscribe(request):
    if request.method  == 'GET':
       to_email = request.GET['email']
       mail_subjectt = 'Subscription confirmation'
       message = '''
       Hello! content pooocha heren, Thank you for subscribing             '''
       send_mail = EmailMessage(mail_subjectt,message,to=[to_email])
       send_mail.send()
    return redirect('home')

