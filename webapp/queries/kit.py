from . import db_connect

def kit_all():
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "Kit"')
            return cur.fetchall()
        
def kit_get(key):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "Kit" WHERE "KitID" = %s', [key])
            return cur.fetchone()
        
def kit_ins(values):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO "Kit" VALUES '
                        '(%s, %s, %s, %s, %s, %s)', values)
            return cur.rowcount
        
def kit_del(key):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM "Kit" WHERE "KitID" = %s', [key])
            return cur.rowcount
