from django.urls import path

from blog_feedback.views import FeedbackFormView, SuccessView

urlpatterns = [
    path('feedback/', FeedbackFormView.as_view(), name='feedback'),
    path('feedback/success/', SuccessView.as_view(), name='feedback_success'),
]
