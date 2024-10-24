from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from .models import ContactMessage

def homepage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact_message = ContactMessage(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            contact_message.save()

            # Redirect to success page or show a message
            return redirect('homepage')
        else:
            print(form.errors)
    else:
        form = ContactForm()

    return render(request, 'Homepage.html', {'form': form})

def contact_success(request):
    return HttpResponse('Thank you for contacting us. We will get back to you soon.')
