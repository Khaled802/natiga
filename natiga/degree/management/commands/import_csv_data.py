import csv

from django.core.management.base import BaseCommand

from degree.models import (  # Replace 'myapp' with the name of your Django app
    Degree
)


def clean(value):
    if value == "null":
        return None
    return value


def clean_image(value):
    if value == "null":
        return "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTwrOqvMw6ggZnvpbjKMenaPA6NLmRNo_re4mklFQHT&s"
    return value


def clean_location(value):
    if value == "null":
        return "Egypt"
    return value


def clean_language_spoken(value):
    if value == "null":
        return "Arabic"
    return value


def clean_review(value):
    if value == "null":
        return 3
    return value


class Command(BaseCommand):
    help = "Imports data from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("csv_file", type=str, help="Path to the CSV file")

    def handle(self, *args, **options):
        csv_file = options["csv_file"]
        # print(__path__)
        with open(f"./degree/management/commands/{csv_file}", encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                person = Degree(
                    seating_number = row['seating_no'],
                    name = row['arabic_name'],
                    student_case = row['student_case'],
                    total_degree = row['total_degree']
                )
                person.save()

        self.stdout.write(self.style.SUCCESS("Data imported successfully"))