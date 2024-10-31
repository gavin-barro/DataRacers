-- Show the race ID, team name, shipment ID, and shipment status for shipments that are currently "In Transit."
CREATE VIEW "RaceTeamShipmentView" AS
SELECT 
    re."RaceID" AS "RaceID",
    t."TeamName" AS "TeamName",
    s."ShipmentID" AS "ShipmentID",
    s."Status" AS "ShipmentStatus"
FROM 
    "Race_Event" re
JOIN 
    "Team" t ON re."RaceID" = t."RaceID"
JOIN 
    "Shipment" s ON re."RaceID" = s."RaceID"
WHERE 
    s."Status" = 'In Transit';

-- SELECT * FROM "RaceTeamShipmentView";
