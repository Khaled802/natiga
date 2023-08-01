from django.db import models
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchHeadline
from django.contrib.postgres.search import TrigramWordDistance
# Create your models here.
class Degree(models.Model):
    seating_number = models.IntegerField(unique=True, db_index=True)
    name = models.CharField(max_length=256)
    student_case = models.SmallIntegerField()
    total_degree = models.FloatField(default=410)

    def __str__(self) -> str:
        return self.name
    
    @classmethod
    def get_by_name(cls, name):
        vector = SearchVector("name", config="arabic")
        query = SearchQuery(name, config='arabic', search_type='phrase')
        return cls.objects.annotate(
          search = vector
        ).filter(search=query)


