from rest_framework.views import APIView, Response

class TestListAPIView(APIView):
    def get(self, request):
        return Response({
            'status': 'ok'
        })