from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Category")


class Store(models.Model):
    store_name = models.CharField(max_length=100)
    text = models.CharField(max_length=100, null=True, blank=True)
    store_img_url = models.CharField(max_length=100, default='', null=True)
    slug = models.SlugField(null=True, blank=True, allow_unicode=True)
    last_modified_date = models.DateField(auto_now=False,null=True,blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    store_logo = models.ImageField(upload_to='stores_images/', verbose_name=_('Image'), null=True, blank=True)

    def __str__(self):
        return self.store_name

    def save(self, *args, **kwargs):
        # if not self.slug:
        self.slug = slugify(self.store_name, allow_unicode=True)
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
        txt=' '
        txt=txt.join([self.store.__str__(),self.offer, self.percentage,f'[{str(converted_date)}]'])
        return txt

    def save(self, *args, **kwargs):
        store = Store.objects.get(slug=self.store.slug)
        print(f'updating {store.slug} {store.last_modified_date}')
        store.last_modified_date = self.last_modified_date
        print(f'updating {store.slug} {store.last_modified_date}')
        store.save()
        super().save(*args, **kwargs)
