from . import db_connect

def kit_all():
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "Kit"')
            return cur.fetchall()