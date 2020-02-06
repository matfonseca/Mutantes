
from code.models import *
from rest_framework import serializers
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('dna','mutant','dna_hash')
