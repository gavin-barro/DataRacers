"""Queries for the Race Events table."""

from . import db_connect


def raceevent_all():
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "Race_Event"')
            return cur.fetchall()


def raceevent_get(key):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM "Race_Event" WHERE "RaceID" = %s', [key])
            return cur.fetchone()


def raceevent_ins(values):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('INSERT INTO "Race_Event" VALUES '
                        '(%s, %s, %s, %s)', values)
            return cur.rowcount

def raceevent_upd(key, values):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('UPDATE "Race_Event" SET "RaceID" = %s, "Location" = %s, '
                        '"Date" = %s, "Creator" = %s', values + [key])
            return cur.rowcount


def raceevent_del(key):
    with db_connect() as conn:
        with conn.cursor() as cur:
            cur.execute('DELETE FROM "Race_Event" WHERE "RaceID" = %s', [key])
            return cur.rowcount


if __name__ == "__main__":
    print("==== First 3 Race Events ====")
    print(raceevent_all()[:3])
