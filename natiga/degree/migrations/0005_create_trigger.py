# Generated by Django 4.2.3 on 2023-08-01 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("degree", "0004_degree_vector_column_and_more"),
    ]

    operations = [
        migrations.RunSQL(
            sql='''
              CREATE TRIGGER vector_column_trigger
              BEFORE INSERT OR UPDATE OF name, vector_column
              ON degree_degree
              FOR EACH ROW EXECUTE PROCEDURE
              tsvector_update_trigger(
                vector_column, 'pg_catalog.arabic', name
              );

              UPDATE degree_degree SET vector_column = NULL;
            ''',

            reverse_sql = '''
              DROP TRIGGER IF EXISTS vector_column_trigger
              ON degree_degree;
            '''
        ),
    ]