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
from django.urls import reverse

from .models import Category, Post,Store
from my_tennis_club import settings


def stores(request):

    posts = Post.objects.all()
    stores = Store.objects.all()
    # noons=Post.objects.filter(store__slug__contains='no')
    # print(noons)
    images_path = os.path.join(settings.STATIC_ROOT, 'img/stores_images/')
    urlss = os.path.join(settings.STATIC_ROOT, 'img', 'urls_txt.css')
    urlss = [url.strip() for url in open(urlss, 'r').readlines()]
    # images = glob(images_path + '/*.*')
    # images_list = []
    # for image in images:
    #     image = Image.open(image)
    #     image64 = image_to_base64(image)
    #     images_list.append(image64)

    flags = os.listdir(os.path.join(settings.STATIC_ROOT, "img/stores_images"))

    flags = ['img/stores_images/' + fl for fl in flags]
    data = {
        'posts': posts,
        'stores': stores,
        'new_stores': stores,
        'new_blogs': stores,
        'page_title': DEFAULT_TITLE,
        'images_list': urlss,
        'images_path': urlss,
        'flags': [],
        'crumbs' : [
                ("جميع المتاجر", reverse('stores')),
                ("جميع المتاجر", reverse('stores')),
                ("جميع المتاجر", reverse('stores')),

            ],

    }
    return render(request, 'store/stores.html', context=data)


def image_to_base64(image):
    buff = BytesIO()
    image.save(buff, format="PNG")
    img_str = base64.b64encode(buff.getvalue())
    img_str = img_str.decode("utf-8")  # convert to str and cut b'' chars
    return img_str


images_path = os.path.join(settings.STATIC_ROOT, 'img/stores_images')

images = glob(images_path + '\*.*')
images_list = []
for image in images:
    image = Image.open(image)
    image64 = image_to_base64(image)
    images_list.append(image64)


DEFAULT_TITLE='موقع كوبونات سيلز لجميع اكواد الخصم الحصرية'
def tgarba(request):
    # print('images_path', images_path)
    # print('rooot', settings.MEDIA_ROOT)

    template = loader.get_template('store/test.html')
    posts = Post.objects.all()
    stores = Store.objects.all()
    images_path = os.path.join(settings.STATIC_ROOT, 'img/stores_images/')
    urlss = os.path.join(settings.STATIC_ROOT, 'img','urls_txt.css')
    urlss=[url.strip() for url in open(urlss,'r').readlines()]
    print(urlss)
    # images = glob(images_path + '/*.*')
    # images_list = []
    # for image in images:
    #     image = Image.open(image)
    #     image64 = image_to_base64(image)
    #     images_list.append(image64)

    flags = os.listdir(os.path.join(settings.STATIC_ROOT, "img/stores_images"))

    flags = ['img/stores_images/' + fl for fl in flags]
    data = {
        'posts': posts,
        'stores': stores,
        'images_list': urlss,
        'images_path': urlss,
        'flags': [],

    }
    print(f'current dir {images}')
    return render(request, 'store/test.html', context=data)


def category_detail(slug):
    template = loader.get_template('store/stores.html')
    cat = Category.objects.get(slug=slug)
    print(cat)
    return HttpResponse(template.render())


def single_store(request,slug):
    posts = Post.objects.filter(store__slug=slug)


    stores = Store.objects.all()
    store = Store.objects.get(slug=slug)
    # Post.objects.filter(las)
    print(f'txt {store.text}')
    # noons=Post.objects.filter(store__slug__contains='no')
    # print(noons)
    for post in posts:
        print(post.last_modified,'ssss')
    images_path = os.path.join(settings.STATIC_ROOT, 'img/stores_images/')
    urlss = os.path.join(settings.STATIC_ROOT, 'img', 'urls_txt.css')
    urlss = [url.strip() for url in open(urlss, 'r').readlines()]
    # images = glob(images_path + '/*.*')
    # images_list = []
    # for image in images:
    #     image = Image.open(image)
    #     image64 = image_to_base64(image)
    #     images_list.append(image64)

    flags = os.listdir(os.path.join(settings.STATIC_ROOT, "img/stores_images"))

    flags = ['img/stores_images/' + fl for fl in flags]
    data = {
        'posts': posts,
        'store': store,
        'store_html': f'{store.html}.html' if store.html else '',
        'posts_count': len(posts),
        'stores': stores,
        'new_stores': stores,
        'page_title': DEFAULT_TITLE,
        'new_blogs': stores,
        'images_list': urlss,
        'images_path': urlss,
        'flags': [],

    }
    return render(request, 'store/store.html', context=data)
