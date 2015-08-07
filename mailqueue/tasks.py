from celery import task
from mailqueue.models import MailerMessage

@task(name="tasks.send_mail")
def send_mail(pk):
    message = MailerMessage.objects.get(pk=pk)
    message.send()
