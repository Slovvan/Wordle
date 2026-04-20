from django.shortcuts import render
from .models import Word
from .serializers import WordSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view

class WordViewSet(ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

@api_view(['GET'])
def daily_word(request):
    word = Word.objects.filter(is_daily=True).first()
    if not word:
        return Response({
            "error": "No daily word found"
            }, status=404)
    return Response(WordSerializer(word).data)

@api_view(['POST'])
def create_word(request):
    serializer = WordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_word(request, pk):
    word = Word.objects.get(pk=pk)
    if not word:
        return Response({
            "error": "Word not found"
            }, status=404)
    serializer = WordSerializer(word, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_word(request, pk):
    word = Word.objects.get(pk=pk)
    if not word:
        return Response({
            "error": "Word not found"
            }, status=404)
    word.delete()
    return Response(status=204)



@api_view(['GET'])
def home(request):
    return render(request, "home.html")
