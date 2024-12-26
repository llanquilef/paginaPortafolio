from rest_framework import serializers
from django.contrib.auth.models import User
from  .models import MultimediaFavorita, RecomendacionUsuario


# User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        
        
# Multimedia Favorita

class MultimediaFavoritaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultimediaFavorita
        fields = ('__all__')
        

# Recomendación Usuario Multimedia

class RecomendacionUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecomendacionUsuario
        fields = ('__all__')
