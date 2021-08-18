from django.db import models
from autoslug import  AutoSlugField
from blog.models import KategoriModel
from django.contrib.auth.models import User

class YazilarModel(models.Model):
    resim = models.ImageField(upload_to="yazi_resimleri")
    baslik = models.CharField(max_length=200)
    icerik = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    duzenleme_tarihi = models.DateTimeField(auto_now=True)
    slug  = AutoSlugField(populate_from= 'baslik', unique=True)
    kategoriler = models.ManyToManyField(KategoriModel, related_name='yazi')
    yazar = models.ForeignKey(User, related_name= 'yazilar', on_delete=models.CASCADE)

    class Meta:
        verbose_name='yazi'
        verbose_name_plural = 'yazilar'
        db_name = 'yazi'