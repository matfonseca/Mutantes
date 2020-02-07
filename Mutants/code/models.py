from django.db import models


class Person(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    dna = models.TextField()
    mutant = models.BooleanField()
    dna_hash = models.IntegerField(null=False
    ) 
    class Meta:
        db_table = 'Person'

    def __str__(self):
        return self.id
    
    def getDnaHash(self):
        return self.dna_hash

    def getDna(self):
        return self.dna
    
    def getMutant(self):
        return self.mutant
