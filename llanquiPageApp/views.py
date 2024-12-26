from django.shortcuts import render
from rest_framework import viewsets
from .models import MultimediaFavorita,RecomendacionUsuario
from .serializers import MultimediaFavoritaSerializer, RecomendacionUsuarioSerializer

# Index

def Index(request):
    return render(request, 'index.html')

# Multimedia Favorita ViewSet 

class MultimediaFavoritaViewSet(viewsets.ModelViewSet):
    queryset = MultimediaFavorita.objects.all()
    serializer_class = MultimediaFavoritaSerializer


# Recomendacion Usuario ViewSet

class RecomendacionUsuarioViewSet(viewsets.ModelViewSet):
    queryset = RecomendacionUsuario.objects.all()
    serializer_class = RecomendacionUsuarioSerializer
    
    
