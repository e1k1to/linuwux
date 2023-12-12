from django.shortcuts import render, HttpResponse

# Create your views here.
def card(request):
  return render(request, "card.html");