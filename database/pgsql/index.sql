CREATE INDEX race_event_raceid ON "Race_Event" ("RaceID");
CREATE INDEX race_event_date ON "Race_Event" ("Date");
CREATE INDEX kitweight ON "Kit" ("TotalWeight");
CREATE INDEX kit_contains ON "Kit" ("KitID")
CREATE INDEX container_status ON "Container"("ContainerStatus")
