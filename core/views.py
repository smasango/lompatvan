# views.py
from django.shortcuts import render
from .forms import ContactForm
from .models import ContactMessage
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .forms import QuoteForm

def homepage(request):
    success_message = None
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact_message = ContactMessage(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone_number=form.cleaned_data['phone_number'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message']
            )
            contact_message.save()

            # Prepare a success message
            success_message = "Your message has been sent successfully!"

            # Re-initialize the form to display a blank form
            form = ContactForm()
        else:
            print(form.errors)
    else:
        form = ContactForm()

    return render(request, 'Homepage.html', {'form': form, 'success_message': success_message})


def contact_success(request):
    return HttpResponse('Thank you for contacting us. We will get back to you soon.')


@require_POST
def submit_quote(request):
    form = QuoteForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'success': True, 'message': 'Your request has been sent successfully!'})
    else:
        # Extract form errors
        errors = form.errors.as_json()
        return JsonResponse({'success': False, 'errors': errors}, status=400)