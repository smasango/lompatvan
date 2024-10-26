from django.db import models
from django.utils.translation import gettext_lazy as _
from zoneinfo import ZoneInfo

class ContactMessage(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    email = models.EmailField(_("Email"), blank=True, null=True)
    phone_number = models.CharField(
        _("Phone Number"),
        max_length=20,
        blank=True,
        null=True,
        help_text=_("Enter your phone number."),
    ) 
    subject = models.CharField(_("Subject"), max_length=200)
    message = models.TextField(_("Messsage"),)
    created_at = models.DateTimeField(_("Created time"),auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    @property
    def formatted_created_at(self):
        """
        Returns the created_at timestamp formatted in the Ireland timezone.
        Example format: '2024-04-27 14:30:00'
        """
        ireland_timezone = ZoneInfo('Europe/Dublin')
        return self.created_at.astimezone(ireland_timezone).strftime('%Y-%m-%d %H:%M:%S')
