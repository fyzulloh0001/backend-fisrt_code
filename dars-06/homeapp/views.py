from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

# Create your views here.
def python(request):
    return render(request=request,template_name='python.html')

def django(request):
    return render(request=request,template_name='django.html')

class base(TemplateView):
    template_name='base.html'