from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404


def home_page(request):
    return render(request, 'blog/landing.html',)
 