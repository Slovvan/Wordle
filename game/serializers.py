from rest_framework.serializers import ModelSerializer
from .models import Word

class WordSerializer(ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'
