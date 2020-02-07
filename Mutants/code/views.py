from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from code.models import *
from code.serializers import *
from code.mutantes import *
import json

class mutantView(generics.CreateAPIView):
    
    queryset = Person.objects.none()
    serializer_class = PersonSerializer

    def get_queryset(self):
        queryset = Person.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        
        #Parametro dna de la resquest
        dna = self.getParam(request) 

        #verificar request Body
        err, message = self.checkBody(dna)
        if(err):
            return Response(message,status = status.HTTP_400_BAD_REQUEST)

        #Busca si el dna ya ha sido ingresado anteriormente
        hash_value = hash(str(dna))
        person = Person.objects.filter(dna_hash = hash_value)
       
       
        if(person.count() == 0): #El dna no ha sido ingresado anteriormente
            mutantDetector = MutantDetector()
        
            if(mutantDetector.isMutant(dna)):
                p = Person(dna = dna, mutant = True, dna_hash = hash_value)
                p.save()
                return Response(status = status.HTTP_200_OK)
            else: 
                p = Person(dna = dna, mutant = False, dna_hash = hash_value)
                p.save()
                return Response(status = status.HTTP_403_FORBIDDEN)

        else: #El dna ya ha sido ingresado anteriormente
            
            isMutant = list(person.values())[0]['mutant'] #Toma el valor de mutant de la query
            if(isMutant):
                return Response(status = status.HTTP_200_OK)
            else:
                return Response(status = status.HTTP_403_FORBIDDEN)

    def getParam(self,request):
        
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        
        if("dna" in body):
            return body["dna"]
        else:
            return ''       
    
    def checkFormat(self,dna):
        #Verifica que la matriz solo contenga las letras (A,T,C,G)
        for row in dna:
            for character in row:
                if(not character in ("A","T","C","G")):
                    return False
        return True
    
    def checkBody(self,dna):
        
        #El body no tiene dna
        if(dna == ''): 
            return True,{"message":"dna not found"}
        
        #Verificion del formato de dna
        if(not self.checkFormat(dna)):
            return True,{"message":"incorrect format, the characters allows are (A,T,C,G)"}

        #Verificacion de dimension
        dim = len(dna)
        if(dim < 4):
            return True,{"message":"incorrect dimension"}
        
        #Verifico que sea cuadrada
        for row in dna:
            if(len(row)!= dim):
                return True, {"message":"matrix isn't square"}
            
        return False,''

class statsView(generics.CreateAPIView):
    
    queryset = Person.objects.none()
    serializer_class = PersonSerializer

    def get_queryset(self):
        queryset = Person.objects.all()
        return queryset

    def create(self, request, *args, **kwargs):
        
        #Obtener la cantidad de humanos y mutantes
        count_mutant_dna = Person.objects.filter(mutant = 1).count()
        count_human_dna = Person.objects.filter(mutant = 0).count()
        
        
        if(count_human_dna == 0): #Si no hay humanos 
            ratio = 0
        else:
            ratio = round(count_mutant_dna/count_human_dna, 3)

        return Response({"count_mutant_dna":count_mutant_dna, 
                         "count_human_dna":count_human_dna, 
                         "ratio":ratio },status = status.HTTP_200_OK)

        













