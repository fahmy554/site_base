import os
import pathlib
from datetime import datetime
from glob import glob

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

from my_tennis_club import settings
from django.templatetags.static import static

# Create your models here.

images_path = os.path.join(settings.BASE_DIR, 'media/stores_images')
images = glob(images_path + '/*.*')

for image in images:
    if 'w200' in image:
        name = image.split('w200_')[-1].split('.')[0].split('-')[0]
    else:
        name = pathlib.Path(image).name.split('.')[0]

    p = os.path.join(settings.BASE_DIR, 'store/templates/store/single_store/')
    name=name.replace('adv_','')
    p = os.path.join(p, f'{name}.html')
    pathlib.Path(p).touch(exist_ok=True)


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Category")


class Store(models.Model):
    store_name = models.CharField(max_length=100)
    html = models.CharField(max_length=100, null=True,unique=True)
    text = models.CharField(max_length=100, null=True, blank=True, default='')
    code = models.CharField(max_length=100, null=True, blank=True, default='')
    store_img_url = models.CharField(max_length=100, default='', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, allow_unicode=True)
    last_modified_date = models.DateField(auto_now=True, null=True, blank=True)
    category = models.ManyToManyField('Category', blank=True, null=True)
    store_logo = models.ImageField(upload_to='stores_images/', verbose_name=_('Image'), null=True, blank=True)

    def __str__(self):
        return self.store_name

    def save(self, *args, **kwargs):
        self.code = self.code.upper()
        images_path = os.path.join(settings.BASE_DIR, 'media/stores_images')
        images = glob(images_path + '/*.*')

        # if not self.slug:
        self.slug = slugify(self.store_name, allow_unicode=True)
        if self.html:
            img = [a for a in images if self.html in a]
            if img:
                self.store_logo.delete(save=False)
                self.store_logo = img[0]
        if not self.store_img_url:
            for img in images:
                # print(self.html, img.lower())
                if self.html in img.lower():
                    img_name = pathlib.Path(img).name
                    # print('img name', img_name)
                    # self.store_img_url=f'/static/img/store_imgs/{img_name}'
                    self.store_img_url = static(f'/img/stores_images/{img_name}')
                    break
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Store")
        verbose_name_plural = _("Stores")


class Store_Image(models.Model):
    Store = models.ForeignKey(Store, on_delete=models.CASCADE, verbose_name=_('Store'))

    # StoreImage = models.ImageField(upload_to='stores_images/', verbose_name=_('Image'))

    def __str__(self):
        return str(self.Store)

    class Meta:
        verbose_name = _("Store_Image")
        verbose_name_plural = _("Store_Images")


class Post(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    txt = models.CharField(max_length=100)
    discount_code = models.CharField(max_length=100, null=True, blank=True)
    offer = models.CharField(max_length=100)
    extra_text = models.CharField(max_length=100, default='كوبون فعال وموثوق', null=True, blank=True)
    percentage = models.CharField(max_length=100)
    last_modified = models.DateTimeField(auto_now=True)
    last_modified_date = models.DateField(auto_now=True)

    class ValidCountries(models.TextChoices):
        EGYPT = "EG", _("EGYPT")
        SUDI = "SA", _("SUDIARABIA")
        JUNIOR = "JR", _("Junior")

    valid_for = models.CharField(max_length=100, choices=ValidCountries.choices, default=ValidCountries.EGYPT)
    valid_until = models.DateTimeField(auto_now=False)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        converted_date = self.last_modified.date()
        txt = ' '
        txt = txt.join([self.store.__str__(), self.offer, self.percentage, f'[{str(converted_date)}]'])
        return txt

    def save(self, *args, **kwargs):
        store = Store.objects.get(slug=self.store.slug)
        print(f'updating {store.slug} {store.last_modified_date}')
        store.last_modified_date = self.last_modified_date
        print(f'updating {store.slug} {store.last_modified_date}')
        store.save()
        super().save(*args, **kwargs)


def make_stores():
    added_htmls = [html[0] for html in Store.objects.values_list('html')]
    print('added html',len(added_htmls))
    print(added_htmls)
    htmls = []
    for image in images:
        if 'w200' in image:
            name = image.split('w200_')[-1].split('.')[0].split('-')[0]
        else:
            name = pathlib.Path(image).name.split('.')[0]
        name=name.replace('adv_','').lower()

        if name in added_htmls or 'sales' in name:
            print(f'passed {name}')
            continue
        htmls.append(name)

    for html in htmls:
        print(f'making store {html}')
        if html in added_htmls:
            print(f'unpdating {html}')
            store=Store.objects.get(html=html)
            store.code='tmp'
        else:
            store=Store(store_name=f'كود خصم {html}')
            store.text='خصومات '
            store.code='tmp'
            store.html=html.lower()
            store.save()
