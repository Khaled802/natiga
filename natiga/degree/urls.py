from django.urls import path
from .views import GetReasultBySeatingNumber, GetReasultByName, GetReasultByNameElstic


urlpatterns = [
    path('seat_number/', GetReasultBySeatingNumber.as_view()),
    path('name/', GetReasultByName.as_view()),
    path('elastic/', GetReasultByNameElstic.as_view()),
]