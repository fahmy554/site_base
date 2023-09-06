from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Category,Post
def index(request):
    template = loader.get_template('store/index.html')
    posts=Post.objects.all()
    data={
        'posts':posts
    }
    return render(request,'store/index.html',context=data)

def tgarba(request):
    template = loader.get_template('store/test.html')
    posts=Post.objects.all()
    data={
        'posts':posts
    }
    return render(request,'store/test.html',context=data)


def category_detail(slug):
    template = loader.get_template('store/index.html')
    cat=Category.objects.get(slug=slug)
    print(cat)
    return HttpResponse(template.render())