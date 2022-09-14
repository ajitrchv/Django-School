from django.urls import path
from .views import HomeView, ThanksView, ContactFormView


app_name = 'classroom'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('thankyou/', ThanksView.as_view(), name="thanks"),
    path('contact/', ContactFormView.as_view(),name='contact'),
    
]
