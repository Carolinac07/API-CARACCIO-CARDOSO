import os
from typing import Generator
import psycopg
from dotenv import load_dotenv

load_dotenv()
passwordDB=os.getenv("SUPABASEPASSWORD")

url=f"postgresql://postgres.djrwsjcdbrssflbndlum:{passwordDB}@aws-1-sa-east-1.pooler.supabase.com:6543/postgres"


def getCursor()-> Generator [psycopg.Cursor, None, None]:
    conn=psycopg.connect(url, sslmode="require")

    cursor=conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()