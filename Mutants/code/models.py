from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    dna = models.TextField()
    mutant = models.BooleanField()
    
    class Meta:
        db_table = 'Person'

    def __str__(self):
        return self.id
