from django.shortcuts import render
from .models import Banner, BannerImage, Service, Gallery
# Create your views here.


def Home(request):
    banner=Banner.objects.order_by('-id').first()
    banner_image=BannerImage.objects.order_by('-id').first()
    services=Service.objects.all()
    gallery=Gallery.objects.all()
    context={
        'banner':banner,
        'banner_image':banner_image,
        'services':services,
        'gallery':gallery,
    }
    return render(request, 'index.html',context)