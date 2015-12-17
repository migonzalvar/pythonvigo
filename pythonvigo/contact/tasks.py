from time import sleep

from django.core.mail import send_mail as django_send_mail

def send_mail(recipient, subject, message):
    recipient_list = [recipient]
    from_email = 'contact@python-vigo.es'
    django_send_mail(subject, message, from_email, recipient_list)
    sleep(3)
