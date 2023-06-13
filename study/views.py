from django.shortcuts import render

# Create your views here.
from django.urls import path, include
from rest_framework.decorators import api_view
from .models import Students, Score
from rest_framework.response import Response
from .serializers import StudentSerializer, ScoreSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def StudentView(request):
   if request.method == 'GET':
      qs = Students.objects.filter()
      serializer = StudentSerializer(qs, many=True)
      return Response(serializer.data)
   elif request.method == 'POST':
       serializer = StudentSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def StudentDetailView(request, pk):

   qs = get_object_or_404(Students, pk=pk)

   if request.method == 'GET':
       serializer = StudentSerializer(qs)
       return Response(serializer.data)
   elif request.method == 'PUT':
       serializer = StudentSerializer(qs, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, 
   status=status.HTTP_400_BAD_REQUEST)
   elif request.method == 'DELETE':
       qs.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def score_view(request):
   if request.method == 'GET':
      qs = Score.objects.filter()
      serializer = ScoreSerializer(qs, many=True)
      return Response(serializer.data)
   elif request.method == 'POST':
         serializer = ScoreSerializer(data=request.data)
         if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def score_detail_view(request, pk):
   
   qs = get_object_or_404(Score, pk=pk)

   if request.method == 'GET':
       serializer = ScoreSerializer(qs)
       return Response(serializer.data)
   elif request.method == 'PUT':
       serializer = ScoreSerializer(qs, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
       return Response(serializer.errors, 
   status=status.HTTP_400_BAD_REQUEST)
   elif request.method == 'DELETE':
       qs.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
   
@api_view(['GET', 'POST'])
def StudentScoreView(request, pk):
    qs = get_object_or_404(Students, pk=pk)
    if request.method == 'GET':
        serializer = ScoreSerializer(qs.score_set.all(), many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(student=qs)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)