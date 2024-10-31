-- query to find a team's kits (in this case the team with the ID 1234).
SELECT *
FROM Team
    JOIN Kit ON Team.TeamID = Kit.TeamID
WHERE Team.TeamID = 1234
  AND Kit.TypeOfKit = 'Team';

-- find the teams at a certain race event (race 57)
SELECT TeamName
FROM Team
    JOIN Race_Event ON Team.RaceID = Race_Event.RaceID
WHERE RaceID = 57;


-- find a container information for a race event and container
SELECT RaceID
FROM Race_Event
	JOIN Shipment ON Race_Event.RaceID = Shipment.RaceID
    JOIN Container ON Shipment.ShipmentID = Container.ShipmentID
WHERE ConID = 12 AND RaceID = 57;

-- Query to find all team kits that are part of a specific container
-- in this case, container 10
SELECT Team_Kit.*, Team_Table.TeamName
FROM Container_contains_TeamKits
    JOIN Team_Kit ON Container_contains_TeamKits.KitID = Team_Kit.KitID
    JOIN Team_Table ON Team_Kit.TeamID = Team_Table.TeamID
WHERE ConID = 10;

-- Query to find the number of containers per shipment
SELECT Shipment.ShipmentID, COUNT(Container.ConID) AS ContainerCount
FROM Shipment
    JOIN Container ON Shipment.ShipmentID = Container.ShipmentID
GROUP BY Shipment.ShipmentID;

-- Query to find each plane shipment arrving at a certain race
SELECT *
FROM Shipment  
    JOIN Race_EVENT ON RaceID
WHERE Method = "Plane"

-- Query to find the number of ships arriving at a race
SELECT COUNT(*)
FROM Shipment
WHERE Destination = "Monaco" and Method = "Ship"

--See all the Team Kits that have arrived in London and have been unloaded--
SELECT TeamName, KitID
FROM Team
	JOIN Kit USING TeamID
	JOIN ContainerContents USING KitID
	JOIN Container USING ConID
	JOIN JOIN Shipment ON ShipmentID
WHERE Container.Status = 'Unloaded'
	AND Shipment.Status = "Arrived"
	AND Shipment.CurrentLocation = "London"
GROUP BY TeamName, KitID

-- Query to count all the critical containers that have arrived at a event
SELECT RaceID, COUNT(ConID)
FROM Race_Event
JOIN Shipment USING RaceID
JOIN Container USING ConID
WHERE Container.Status = "Arrived" AND
	Container.CriticalContainer = True;
