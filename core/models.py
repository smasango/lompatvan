# models.py
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
    message = models.TextField(_("Message"))
    created_at = models.DateTimeField(_("Created time"), auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    @property
    def formatted_created_at(self):
        ireland_timezone = ZoneInfo('Europe/Dublin')
        return self.created_at.astimezone(ireland_timezone).strftime('%Y-%m-%d %H:%M:%S')


class Quote(models.Model):
    from_location = models.CharField(max_length=50)
    to_location = models.CharField(max_length=50)
    other1 = models.CharField(max_length=50, blank=True, null=True)
    other2 = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'Quote from {self.name}'


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_subscribed']

    def __str__(self):
        return self.email