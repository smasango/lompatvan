# forms.py
from django import forms
import phonenumbers
from phonenumbers import NumberParseException
from phonenumbers.phonenumberutil import PhoneNumberType
from .models import Quote
import re

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name',
            'style': 'height: 55px;',
        })
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Email',
            'style': 'height: 55px;',
        }),
        help_text='Optional: Enter your email address.'
    )
    phone_number = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Phone Number',
            'style': 'height: 55px;',
        }),
        help_text='Optional: Enter your phone number.'
    )
    subject = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Subject',
            'style': 'height: 55px;',
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Message',
            'style': 'height: 55px;',
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')

        if not email and not phone_number:
            raise forms.ValidationError('Please provide either an email address or a phone number.')

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            phone = re.sub(r'[ \-\(\)]', '', phone_number)
    
            # Define regex patterns
            mobile_local_pattern = r'^08[1-9]\d{7}$'
            mobile_international_pattern = r'^\+3538[1-9]\d{7}$'
            
            landline_local_pattern = r'^0[1-57-9]\d{6,8}$'
            landline_international_pattern = r'^\+353[1-57-9]\d{6,8}$'
            
            # Check for Mobile Local
            if re.match(mobile_local_pattern, phone):
                return  phone
            
            # Check for Mobile International
            if re.match(mobile_international_pattern, phone):
                return  phone
            
            # Check for Landline Local
            if re.match(landline_local_pattern, phone):
                return  phone
            
            # Check for Landline International
            if re.match(landline_international_pattern, phone):
                return  phone
            
            # If none of the patterns match, raise ValidationError
            raise forms.ValidationError('Enter a valid Irish phone number.')

        return phone_number

class QuoteForm(forms.ModelForm):
    from_location = forms.CharField(
        max_length=20,
        error_messages={
            'invalid': 'Please add a valid location.',
            'required': 'Pick-up location is required.'
        }
    )
    to_location = forms.CharField(
        max_length=20,
        error_messages={
            'invalid': 'Please add a valid location.',
            'required': 'Drop-off location is required.'
        }
    )
    other1 = forms.CharField(max_length=50, required=False)
    other2 = forms.CharField(max_length=50, required=False)

    class Meta:
        model = Quote
        fields = ['from_location', 'to_location', 'name', 'phone', 'email', 'message', 'other1', 'other2']

    def clean_phone(self):
        phone_number = self.cleaned_data.get('phone')
        if phone_number:
            phone = re.sub(r'[ \-\(\)]', '', phone_number)
    
            # Define regex patterns
            mobile_local_pattern = r'^08[1-9]\d{7}$'
            mobile_international_pattern = r'^\+3538[1-9]\d{7}$'
            
            landline_local_pattern = r'^0[1-79]\d{6,8}$'
            landline_international_pattern = r'^\+353[1-79]\d{6,8}$'
            
            # Check for Mobile Local
            if re.match(mobile_local_pattern, phone):
                return  phone
            
            # Check for Mobile International
            if re.match(mobile_international_pattern, phone):
                return  phone
            
            # Check for Landline Local
            if re.match(landline_local_pattern, phone):
                return  phone
            
            # Check for Landline International
            if re.match(landline_international_pattern, phone):
                return  phone
            
            # If none of the patterns match, raise ValidationError
            raise forms.ValidationError('Enter a valid Irish phone number.')

        return phone_number

    