from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Degree


@registry.register_document
class CarDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'degrees'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Degree # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'seating_number', 'name', 'student_case', 'total_degree'
        ]