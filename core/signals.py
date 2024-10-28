from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage, Quote

import logging

logger = logging.getLogger(__name__)

@receiver(post_save, sender=ContactMessage)
def send_contact_message_notification(sender, instance, created, **kwargs):
    if created:
        # The email details
        subject = f"New Contact Message from {instance.name}"
        message = f"""
        You have received a new message from your website's contact form.

        Name: {instance.name}
        Phone Number: {instance.phone_number}
        Subject: {instance.subject}
        
        Message:
        {instance.message}

        Sent on: {instance.formatted_created_at}
        """
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.DEFAULT_RECIPIENT_EMAIL, 'smasango@gmail.com', 'advisorayush@gmail.com']

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)
            customer_update(instance.email, instance.name)
        except Exception as e:
            logger.error(f"Failed to send contact message email: {e}")


@receiver(post_save, sender=Quote)
def send_contact_message_notification(sender, instance, created, **kwargs):
    if created:
        subject = f"New Quote Request from {instance.name}"
        message = f"""
        You have received a new Quote request from your website's Quote form.

        Name: {instance.name}
        Phone Number: {instance.phone}
        from: {instance.from_location}
        to: {instance.to_location}
        
        Message:
        {instance.message}

        """
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.DEFAULT_RECIPIENT_EMAIL, 'smasango@gmail.com']

        try:
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)
            customer_update(instance.email, instance.name)
        except Exception as e:
            logger.error(f"Failed to send contact message email: {e}")

def customer_update(recipient, name):
    subject="Your Quote Request with TSBVANS!!"
    message=f"""
    Dear {name},

    Thank you for reaching out to TSBVANS! We appreciate your interest in our services. A member of our team will review your request and get back to you as soon as possible with a detailed quote. Please feel free to share any specific details about your move or delivery needs if you haven't already.
    
    Best regards,
    TSBVANS
    """
    rc_list = [recipient,]
    from_email = settings.DEFAULT_FROM_EMAIL
    send_mail(subject, message, from_email, rc_list, fail_silently=True)