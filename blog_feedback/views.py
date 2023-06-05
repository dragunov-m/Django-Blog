from blog_feedback.forms import FeedbackForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView


class FeedbackFormView(FormView):
    template_name = "blog_feedback/feedback.html"
    form_class = FeedbackForm
    success_url = "/success/"

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "blog_feedback/success.html"
