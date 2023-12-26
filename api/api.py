from api.models import chambeador
from rest_framework import viewsets, permissions
from .serializer import chambeadorSerializer

class chambeadorViewSet(viewsets.ModelViewSet):
    queryset = chambeador.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = chambeadorSerializer