# forms.py
from django import forms
import phonenumbers
from phonenumbers import NumberParseException
from .models import Quote

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
            raise forms.ValidationError('Either email or phone number must be provided.')

    # forms.py
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            try:
                # Parse the phone number without a default region
                parsed_number = phonenumbers.parse(phone_number, None)
                # Check if the number is valid
                if not phonenumbers.is_valid_number(parsed_number):
                    raise forms.ValidationError('Enter a valid Irish phone number.')
                # Ensure the number belongs to Ireland
                region_code = phonenumbers.region_code_for_number(parsed_number)
                if region_code != 'IE':
                    raise forms.ValidationError('Enter a valid Irish phone number.')
            except NumberParseException:
                raise forms.ValidationError('Enter a valid Irish phone number.')
        return phone_number


class QuoteForm(forms.ModelForm):
    from_location = forms.CharField(
        max_length=20,
        error_messages={
            'invalid': 'Please Add a valid location',
            'required': 'Pick-Up location is required'
        }
    )
    to_location = forms.CharField(
        max_length=20,
        error_messages={
            'invalid': 'Please Add a valid location',
            'required': 'Drop-Off location is required'
        }
    )
    class Meta:
        model = Quote
        fields = ['from_location', 'to_location', 'name', 'phone', 'email', 'message']

    def clean_phone(self):
        phone_number = self.cleaned_data.get('phone')
        if phone_number:
            try:
                first_char = phone_number[0]
    
                if first_char == '0':
                    phone_number = '+353' + phone_number[1:]
                elif not (first_char.isdigit() or first_char == '+'):
                    raise forms.ValidationError("Invalid first character", first_char)
                    
                # Parse the phone number with default region 'IE' (Ireland)
                parsed_number = phonenumbers.parse(phone_number, 'IE')
                
                # Check if the number is valid
                if not phonenumbers.is_valid_number(parsed_number):
                    raise forms.ValidationError('Enter a valid Irish phone number.')
                
                # Ensure the number belongs to Ireland
                region_code = phonenumbers.region_code_for_number(parsed_number)
                if region_code != 'IE':
                    raise forms.ValidationError('Enter a valid Irish phone number.')
            except NumberParseException:
                raise forms.ValidationError('Enter a valid Irish phone number.')
        return phone_number




