from . import db_connect

def shipment_all():
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "Shipment"')
            return cur.fetchall()
        
def shipment_get(key):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "Shipment" WHERE "ShipmentID" = %s', [key])
            return cur.fetchone()
        
def shipment_ins(values):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO "Shipment" VALUES '
                        '(%s, %s, %s, %s, %s, %s ,%s)', values)
            return cur.rowcount
        
def shipment_del(key):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM "Shipment" WHERE "ShipmentID" = %s', [key])
            return cur.rowcount