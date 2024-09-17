from django.urls import path, include
from prototype.verification_by_image_input import urls as image_input_urls

urlpatterns = [
    path('input_image/', include(image_input_urls)),
]