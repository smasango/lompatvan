from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('contact-success/', views.contact_success, name='contact_success'),
    path('submit-quote/', views.submit_quote, name='submit_quote'),
    path('success/',views.success, name='success')
]
