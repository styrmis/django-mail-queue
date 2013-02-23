from django.contrib import admin
from django.conf import settings

from .models import MailerMessage, Attachment
from . import defaults

__author__ = 'Derek Stegelman'
__date__ = '10/5/12'


class AttachmentAdmin(admin.TabularInline):
    model = Attachment
    extra = 1


class MailerAdmin(admin.ModelAdmin):
    list_display = ('app', 'subject', 'to_address', 'sent', 'last_attempt')
    search_fields = ['to_address', 'subject', 'app', 'bcc_address', 'content']
    fields = (('to_address', 'from_address', 'bcc_address'), 'subject', 'content', 'html_content', 'app',
              'last_attempt')
    actions = ['send_failed']
    list_filter = ('sent', 'last_attempt', 'app')
    inlines = [AttachmentAdmin]
    readonly_fields = ['last_attempt']

    def send_failed(self, request, queryset):
        emails = queryset.filter(sent=False)
        for email in emails:
            if getattr(settings, 'MAILQUEUE_CELERY', defaults.MAILQUEUE_CELERY):
                from mailqueue.tasks import send_mail
                send_mail.delay(email)
            else:
                email.send()
        self.message_user(request, "Emails queued.")

admin.site.register(MailerMessage, MailerAdmin)