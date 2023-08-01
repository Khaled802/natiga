# Natiga 
it is a populate the degrees of (secondary school degree), and add search by seating number and the name

## tools
   - Django
   - django rest framework
   - Postgres
   - elastic-search

## how to populate file .csv using Django
   1. In the app `degree`, we made folder named `management`
   2. add new folder inside `management` called `commands`
   3. in both folders add an empty file `__init__.py`
   4. put the file `import_csv_data.py` in this file you will read the .csv file and create record for each row
   5. you should import the model you want to populate and use it in the file
   6. you should choose the path of .csv file in `with open('path')`
   7. in open I add encoded because I read arabic names
   8. map each raw name with the model attribute (for example: in .csv seating_no and I name it in model seating_number)
   9. run ```python manage.py import_csv_data``` \<csv name\> (example: `python manage.py import_csv_data nn.csv`)
   10. wait until you see `Data imported successfully`


## how to use elasticsearch in Django
   1. you should have elasticsearch run on your machine, I perfere using Docker
   2. install `django-elasticsearch-dsl`
   3. add `django_elasticsearch_dsl` to INSTALLED_APPS in settings.py
   4. add this config in settings.py
      ```python
      ELASTICSEARCH_DSL={
         'default': {
            'hosts': 'localhost:9200'
         },
      }
      ```
   5. start to build the document as shown in `degree/document` and add the model to it and name the index and choose the fields that you want
   6. you will need to build the index to search from it 
   ```powershell
      python manage.py search_index --rebuild
   ```
   7. that will take time as the size of the data
   8. go to the view and make the query 
   9. add the view to url to excute it

   

