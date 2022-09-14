from operator import contains
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from classroom.forms import ContactForm
# Create your views here.
# def home(request):
#     return render(request,'classroom/home.html')

class HomeView(TemplateView):
    template_name= 'classroom/home.html'
    
class ThanksView(TemplateView):
    template_name= 'classroom/thankyou.html'
    
class ContactFormView(FormView):
    form_class = ContactForm
    template_name='classroom/contact.html'
    
    success_url = "/classroom/thankyou/"
    
    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)
       
    