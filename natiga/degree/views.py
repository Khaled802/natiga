from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .serializers import DegreeSerializer, GettingResultBySeatingNumber, GettingResultByName
from .models import Degree
from django.shortcuts import get_object_or_404

# Create your views here.

class GetReasultBySeatingNumber(APIView):
    def get(self, request: Request) -> Response:

        serialize_input = GettingResultBySeatingNumber(data=request.query_params)
        serialize_input.is_valid(raise_exception=True)
        seating_number = int(dict(GetReasultByName(data=request.query_params).data)['seating_number'][0])

        degree = get_object_or_404(Degree, seating_number=seating_number)
        serialized_degree = DegreeSerializer(degree)
        return Response(serialized_degree.data, status=status.HTTP_200_OK)


class GetReasultByName(APIView):
    def get(self, request: Request) -> Response:

        serialize_input = GettingResultByName(data=request.query_params)
        serialize_input.is_valid(raise_exception=True)
        name = dict(request.query_params)['name'][0]

        degree = Degree.get_by_name(name)
        serialized_degree = DegreeSerializer(degree, many=True)
        return Response(serialized_degree.data, status=status.HTTP_200_OK)

from elasticsearch_dsl import Search, Q

def search_by_name(query_name):
    # Create an Elasticsearch search object
    search = Search(index='degrees')  # Replace 'your_index_name' with your actual index name

    # Define an analyzer for the name field (you can adjust this based on your needs)
    name_analyzer = 'standard'  # You can use 'english', 'french', or a custom analyzer

    # Create a query for the name field using fuzzy matching and boosting
    name_query = Q(
        'match',
        name={
            'query': query_name,
            'fuzziness': 'AUTO',  # Allow fuzzy matching
            'boost': 2.0,  # Boost the relevance score for the name field
            'analyzer': name_analyzer,
        }
    )

    # Create a query for the name field using phrase matching
    phrase_query = Q(
        'match_phrase',
        name={
            'query': query_name,
            'slop': 2,  # Allow a small distance between words in the name
            'analyzer': name_analyzer,
        }
    )

    # Combine the queries with 'should' (OR) to get more diverse results
    search = search.query(name_query | phrase_query)

    # Execute the search and get the results
    response = search.execute()

    # Process the results and return them
    results = []
    for hit in response.hits:
        results.append(hit.to_dict())

    return results


class GetReasultByNameElstic(APIView):
    def get(self, request: Request) -> Response:

        serialize_input = GettingResultByName(data=request.query_params)
        serialize_input.is_valid(raise_exception=True)
        name = dict(request.query_params)['name'][0]

        degree = search_by_name(name)
        serialized_degree = DegreeSerializer(degree, many=True)
        return Response(serialized_degree.data, status=status.HTTP_200_OK)