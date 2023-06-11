from django.core.mail import send_mail
# from blog_feedback.tasks import send_feedback_email_task
from django import forms


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    recipient_email = forms.EmailField()
