from . import db_connect


def person_all():
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "Person"')
            return cur.fetchall()
        
def person_get(key):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "Person" WHERE "PersonID" = %s', [key])
            return cur.fetchone()
        
def person_ins(values):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO "Person" VALUES '
                        '(%s, %s, %s, %s, %s)', values)
            return cur.rowcount
        
def person_upd(key, values):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('UPDATE "Person" SET "PersonID" = %s, "Name" = %s, '
                        '"KitID" = %s, "PhoneNum" = %s, "Permissions" = %s WHERE "PersonID" = %s', values + [key] )
            return cur.rowcount

def person_del(key):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM "Person" WHERE "PersonID" = %s', [key])
            return cur.rowcount