from fastapi import APIRouter
import psycopg2
from os import getenv
from fastapi.responses import ORJSONResponse

router = APIRouter()


@router.get('/get_data')
async def get_bridges_data():
    conn = psycopg2.connect(
        dbname=getenv("DBNAME"),
        user=getenv("USER"),
        password=getenv("PASSWORD"),
        host=getenv("HOST"),
        port=getenv("PORT")
    )

    with conn:
        cur = conn.cursor()
        cur.execute("""
        SELECT json_agg(row_to_json(bridges_data))
        FROM bridges_data;
        """)

        return ORJSONResponse(cur.fetchall()[0][0])
