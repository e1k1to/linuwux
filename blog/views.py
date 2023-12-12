from django.shortcuts import render
from .models import postzinho

# Create your views here.
def blog(request):
  items = postzinho.objects.all()
  return render(request, "blog.html", {"posts": items });
