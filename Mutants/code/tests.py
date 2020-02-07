from django.test import TestCase
from code.models import Person
from code.mutantes import *
import random
from django.test import RequestFactory, TestCase
from code.views import mutantView
import json

class PersonTestCase(TestCase):
    def setUp(self):
        Person.objects.create(dna ="[ATGCGA,CAGTGC,TTATGT,AGAAGG,CCCCTA,TCACTG]", mutant = True,dna_hash = 1234)
        

    def test_get_dnsHash(self):
        
        person = Person.objects.get(dna_hash = 1234)
        
        self.assertEqual(person.getDnaHash(), 1234)
    
    def test_get_Mutant(self):
        person = Person.objects.get(dna_hash = 1234)
        self.assertEqual(person.getMutant(), True)

    def test_get_dna(self):
        person = Person.objects.get(dna_hash = 1234)
        self.assertEqual(person.getDna(), "[ATGCGA,CAGTGC,TTATGT,AGAAGG,CCCCTA,TCACTG]")
    
class MuntantDectectorCase(TestCase):
    
    def test_isMutant_True(self):
        
        dna_mutant =["ATGCGA",
                     "CAGTGC",
                     "TTATGT",
                     "AGAAGG",
                     "CCCCTA",
                     "TCACTG"]

        mutantDectector = MutantDetector()

        self.assertTrue(mutantDectector.isMutant(dna_mutant))

    def test_isMutant_False(self):
        
        dna_human =["ATGCGA",
                    "CCGTTC",
                    "TTATGT",
                    "AGAAGG",
                    "CCCCTA",
                    "TCACTG"]
        
        mutantDectector = MutantDetector()

        self.assertTrue( not mutantDectector.isMutant(dna_human))


class MutantApi(TestCase):
    def setUp(self):
       
        self.factory = RequestFactory()
       
    def test_isMutant_True(self):
       
        request = self.factory.post('/mutant/', data = { "dna":["ATGCGA",
                     "CAGTGC",
                     "TTATGT",
                     "AGAAGG",
                     "CCCCTA",
                     "TCACTG"]}, content_type='application/json')

        response = mutantView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_isMutant_False(self):
       
        request = self.factory.post('/mutant/', data = { "dna":["TTGCGA",
                 "CAGTTC",
                 "TTAAGT",
                 "ATAAGG",
                 "CCCCTA",
                 "TCACTG"]}, content_type='application/json')

        response = mutantView.as_view()(request)
        self.assertEqual(response.status_code, 403)
    
    def test_isMutant_false_500dnas(self):
        testBoolean = True
        dnas = jsonfileToDic("code/data/dnasHuman.json")
        
        for dna in dnas.values():
            request = self.factory.post('/mutant/', data = { "dna":dna}, content_type='application/json')

            response = mutantView.as_view()(request)

            if(response.status_code != 403):
                testBoolean = False

        for dna in dnas.values():
            request = self.factory.post('/mutant/', data = { "dna":dna}, content_type='application/json')

            response = mutantView.as_view()(request)

            if(response.status_code != 403):
                testBoolean = False
        
        self.assertTrue(testBoolean)

def jsonfileToDic(filename):
    with open(filename,'r') as f_in:
        return(json.load(f_in))