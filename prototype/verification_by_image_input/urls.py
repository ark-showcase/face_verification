from django.urls import path, include
from prototype.verification_by_image_input.views import FaceVerification

urlpatterns = [
    path('verify/', FaceVerification.as_view(), name='verify_by_image_file'),
]