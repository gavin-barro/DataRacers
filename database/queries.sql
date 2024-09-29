-- query to find a team's kits (in this case the team with the ID 1234).
SELECT *
FROM Team_Table
    JOIN Team_Kit ON Team_Table.TeamID = Team_Kit.TeamID
WHERE Team_Table.TeamID = 1234;

-- find the teams at a certain race event (race 57)
SELECT TeamName
FROM Team_Table
    JOIN Race_Event ON Team_Table.RaceID = Race_Event.RaceID
WHERE RaceID = 57;