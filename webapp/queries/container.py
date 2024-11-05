"""Queries for the Container table."""

from . import db_connect

def container_all():
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "Container"')
            return cur.fetchall()

def container_get(key):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "Container" WHERE "ConID" = %s', [key])
            return cur.fetchone()

def container_ins(values):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO "Container" VALUES '
                        ' (%s, %s, %s, %s, %s)', values)
            return cur.rowcount

def container_upd(key, values):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('UPDATE "Container" SET "ShipmentID" = %s, "CriticalContainer" = %s, '
                        '"Status" = %s, "UpdatedBy" = %s WHERE "ConID" = %s', values + [key])
            return cur.rowcount

def container_del(key):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM "Container" WHERE "ConID" = %s', [key])
            return cur.rowcount

# if __name__ == "__main__":
#     print("==== First 3 Containers ====")
#     print(container_all()[:3])
