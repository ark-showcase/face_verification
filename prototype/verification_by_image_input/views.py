from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class FaceVerification(APIView):
    def get(self, request):
        return render(request,'home.html', context={})