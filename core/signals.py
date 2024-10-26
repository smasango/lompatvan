from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage

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
            send_mail(subject, message, from_email, recipient_list)
        except Exception as e:
            logger.error(f"Failed to send contact message email: {e}")
