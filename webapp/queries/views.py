"""Queries for database views."""

from . import db_connect

def critical_dates(race_year):
    with db_connect() as con:
        with con.cursor() as cur:
            cur.execute("""SELECT
	    re."RaceID",
	    re."Location",
	    re."Date",
	    s."ShipmentID",
	    s."Status" AS "Shipment Status",
	    c."ConID" AS "Critical ContainerID"
	FROM "Race_Event" re
	JOIN "Shipment" s ON re."RaceID" = s."RaceID"
	JOIN "Container" c ON s."ShipmentID" = c."ShipmentID"
	WHERE re."Date" BETWEEN '%s-01-01' 
		AND '%s-12-31'  
	    AND s."Status" = 'Not Left'                      
	    AND c."CriticalContainer" = TRUE;""", [race_year])
            return cur.fetchall()