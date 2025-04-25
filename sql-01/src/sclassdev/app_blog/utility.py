from django.db import connection

def query(query="", params=[]):
    with connection.cursor() as cursor:
        cursor.execute(query, params)

        if query.strip().lower().startwith("select"):
            return dictfetchall(cursor)
        else:
            return None
        
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    columns = [col[0] for col in cursor.description]

    return [dict(zip(columns, row)) for row in cursor.fetchall()]