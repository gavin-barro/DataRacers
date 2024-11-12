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

--
-- View UPCOMING critical shipments for a Race Event in 2024(Or specified year)
--
CREATE VIEW UpcomingCriticalShipments AS
	SELECT
	    re."RaceID",
	    re."Location",
	    re."Date",
	    s."ShipmentID",
	    s."Status" AS "Shipment Status",
	    c."ConID" AS "Critical ContainerID"
	FROM "Race_Event" re
	JOIN "Shipment" s ON re."RaceID" = s."RaceID"
	JOIN "Container" c ON s."ShipmentID" = c."ShipmentID"
	WHERE re."Date" BETWEEN '2024-01-01' 
		AND '2024-12-31'  
	    AND s."Status" = 'Not Left'                      
	    AND c."CriticalContainer" = TRUE; 

---View Kits that are over the maximum weight (10 in this example),
---and the information of the person responsible for the kit
CREATE VIEW "OverweightKits" AS
SELECT
	c."ConID" as "Container ID",
	k."KitID" as "Kit ID",
	k."TypeOfKit" as "Type Of Kit",
	k."TotalWeight" as "Weight of Kit",
	p."Name" as "Owner of Kit",
	p."PhoneNum" as "Owner Phone Number"
FROM "Container" c
	JOIN "ContainerContents" cc ON c."ConID" = cc."ConID"
	JOIN "Kit" k ON k."KitID" = cc."KitID"
	JOIN "Person" p ON k."OwnerID" = p."PersonID"
WHERE "TotalWeight" > 10

