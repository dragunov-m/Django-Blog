from blog_feedback.forms import EmailForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from blog_feedback.tasks import send_email_task


class FeedbackFormView(FormView):
    template_name = "blog_feedback/feedback.html"
    form_class = EmailForm
    success_url = "/feedback/success/"

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        recipient_list = [form.cleaned_data['recipient_email']]
        from_email = 'contact.mendelson@gmail.com'

        send_email_task.delay(subject, message, from_email, recipient_list)

        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "blog_feedback/success.html"
