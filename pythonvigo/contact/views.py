from time import sleep

from django.core.mail import send_mail
from django import forms
from django.shortcuts import render, redirect

class ContactForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()

    def send_mail(self):
        subject = 'Contact form'
        message = 'Thank you'
        from_email = 'contact@python-vigo.es'
        recipient_list = [self.cleaned_data['email']]
        sleep(3)
        send_mail(subject, message, from_email, recipient_list)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_mail()
            return redirect('thanks')
    if request.method == 'GET':
        form = ContactForm()
    return render(request, 'contact/contact_form.html', {'form': form})


def thank_you(request):
    return render(request, 'contact/contact_success.html')
