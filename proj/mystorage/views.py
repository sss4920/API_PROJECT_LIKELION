from rest_framework import viewsets
from .models import Essay
from .serealizers import EssaySerealizer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all()
    serializer_class = EssaySerealizer