from fastapi import APIRouter
import psycopg2
from os import getenv

router = APIRouter()

# Connect to database
conn = psycopg2.connect(
    dbname=getenv('DBNAME'),
    user=getenv('USER'),
    password=getenv('PASSWORD'),
    host=getenv('HOST'),
    port=getenv('PORT'),
)


@router.get('/get_data')
async def get_bridges_data():

    # Instantiate cursor
    cur = conn.cursor()

    # Execute query
    cur.execute("""
    SELECT row_to_json(bridges_data)
    FROM bridges_data;
    """)

    # Return list of JSON
    return [query[0] for query in cur.fetchall()]
