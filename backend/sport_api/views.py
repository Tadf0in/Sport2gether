from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import Sport
from .serializers import SportSerializer

from drf_yasg.utils import swagger_auto_schema


class SportView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    @swagger_auto_schema(
        responses = {
            200: SportSerializer
        }
    )
    def get(self, request):
        sports = Sport.objects.all()
        serializer = SportSerializer(sports, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # def post(self, request):
    #     serializer = SportSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)