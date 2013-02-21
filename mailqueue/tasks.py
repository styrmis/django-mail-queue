from celery.task import task


@task()
def send_mail(mailer):
    mailer.send()
