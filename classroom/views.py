from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
# def home(request):
#     return render(request,'classroom/home.html')

class HomeView(TemplateView):
    template_name= 'classroom/home.html'
    
class ThanksView(TemplateView):
    template_name= 'classroom/thankyou.html'
    