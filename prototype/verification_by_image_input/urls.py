from django.urls import path, include
from prototype.verification_by_image_input.views import TakeFace

urlpatterns = [
    path('take-face/', TakeFace.as_view(), name='take_face'),
    path('verify-face/', TakeFace.as_view(), name='verify_face'),
]