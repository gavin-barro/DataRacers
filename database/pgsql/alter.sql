ALTER TABLE "Team" ADD FOREIGN KEY ("RaceID") REFERENCES "Race_Event" ("RaceID");

ALTER TABLE "ContainerContents" ADD FOREIGN KEY ("ConID") REFERENCES "Container" ("ConID");

ALTER TABLE "Kit" ADD FOREIGN KEY ("KitID") REFERENCES "ContainerContents" ("KitID");

ALTER TABLE "Container" ADD FOREIGN KEY ("ShipmentID") REFERENCES "Shipment" ("ShipmentID");

ALTER TABLE "Shipment" ADD FOREIGN KEY ("RaceID") REFERENCES "Race_Event" ("RaceID");

ALTER TABLE "TeamKit_Manager" ADD FOREIGN KEY ("PersonID") REFERENCES "Person" ("PersonID");

ALTER TABLE "Race_Event" ADD FOREIGN KEY ("Creator") REFERENCES "Race_Event_Organizer" ("OrganizerID");

ALTER TABLE "Shipment" ADD FOREIGN KEY ("CreatedBy") REFERENCES "Race_Event_Organizer" ("OrganizerID");

ALTER TABLE "RaceCrew_Member" ADD FOREIGN KEY ("PersonID") REFERENCES "Person" ("PersonID");

ALTER TABLE "TeamKit_Manager" ADD FOREIGN KEY ("TeamID") REFERENCES "Team" ("TeamID");

ALTER TABLE "Kit" ADD FOREIGN KEY ("OwnerID") REFERENCES "Person" ("PersonID");

ALTER TABLE "Kit" ADD FOREIGN KEY ("TeamID") REFERENCES "Team" ("TeamID");

ALTER TABLE "KitContents" ADD FOREIGN KEY ("KitID") REFERENCES "Kit" ("KitID");