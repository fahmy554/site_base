import base64
import os
from glob import glob
from io import BytesIO

from PIL import Image
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Category, Post


def index(request):
    template = loader.get_template('store/index.html')
    posts = Post.objects.all()
    data = {
        'posts': posts
    }
    return render(request, 'store/index.html', context=data)


def image_to_base64(image):
    buff = BytesIO()
    image.save(buff, format="PNG")
    img_str = base64.b64encode(buff.getvalue())
    img_str = img_str.decode("utf-8")  # convert to str and cut b'' chars
    return img_str


images_path = os.path.join(os.getcwd(), 'static\img\stores_images')
images = glob(images_path + '\*.*')
images_list = []
for image in images:
    image = Image.open(image)
    image64 = image_to_base64(image)
    images_list.append(image64)


def tgarba(request):
    template = loader.get_template('store/test.html')
    posts = Post.objects.all()

    data = {
        'posts': posts,
        'images_list': images_list

    }
    print(f'current dir {images}')
    return render(request, 'store/test.html', context=data)


def category_detail(slug):
    template = loader.get_template('store/index.html')
    cat = Category.objects.get(slug=slug)
    print(cat)
    return HttpResponse(template.render())
