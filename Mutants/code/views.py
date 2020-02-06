from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics


from code.models import *
from rest_framework import viewsets
from code.serializers import *
from code.mutantes import *
from django.db.models import Avg, Count, Min, Sum
import json

class mutantView(generics.ListCreateAPIView):
    """
    API endpoint that allows multiple members to be created.
    """
    queryset = Person.objects.none()
    serializer_class = PersonSerializer

    def get_queryset(self):
        queryset = Person.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        
        dna = self.getParam(request) 

        if(dna == ''):
            return Response({"message":"dna not found"},status = status.HTTP_400_BAD_REQUEST)

        mutantDetector = MutantDetector()
       
        if(mutantDetector.isMutant(dna)):
            p = Person(dna = dna, mutant = True)
            p.save()
            return Response(status = status.HTTP_200_OK)
        else:
            p = Person(dna = dna, mutant = False)
            p.save()
            return Response(status = status.HTTP_403_FORBIDDEN)
    
    def getParam(self,request):
        
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        if("dna" in body):
            return body["dna"]
        else:
            return ''       








