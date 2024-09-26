from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from prototype.face_verifier.recognition import FaceRecognition

class TakeFace(APIView):
    def get(self, request):
        return render(request,'home.html', context={})

class VerifyFace(APIView):
    def get(self, request):
        image_file = request.FILES.get('image')
        print(image_file)
        fr_obj = FaceRecognition('prototype/face_verifier/testImage/224635_1692255109665_1503057_n.jpg')
        print(f'from views: {fr_obj.find_match()}')
        return Response({'message': 'hello world'})
