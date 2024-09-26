from django.urls import path, include
from prototype.verification_by_image_input.views import TakeFace, VerifyFace

urlpatterns = [
    path('take-face/', TakeFace.as_view(), name='take_face'),
    path('verify-face/', VerifyFace.as_view(), name='verify_face'),
]