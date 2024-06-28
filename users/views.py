from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .conversor import UserSerializer
from django.core.management import call_command
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
@permission_classes([IsAdminUser])
def fetch_users_view(request):
    try:
        call_command('consulta')
        return Response({"message": "Usuários obtidos com sucesso"}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"erro": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
