from django import forms
from django.shortcuts import render, redirect

from contact.tasks import send_mail

class ContactForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()

    def send_mail(self):
        recipient = self.cleaned_data['email']
        subject = 'Contact form'
        message = 'Thank you'
        send_mail.delay(recipient, subject, message)

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
