from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
def home(request):
   return render(request, 'static_handler.html')
   #return render(request, 'index.html')
   #return HttpResponse("Привет, Мир!", content_type='text/plain; charset=utf-8')
   #return HttpResponse(u'Привет, Мир!', content_type="text/plain")
   #return HttpResponse(u'Привет, Мир!')

# Create your views here.