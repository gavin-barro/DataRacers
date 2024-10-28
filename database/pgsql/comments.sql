COMMENT ON TABLE "Race_Event" IS 'This table contains general information about the race';

COMMENT ON COLUMN "Race_Event"."RaceID" IS 'The current race';

COMMENT ON COLUMN "Race_Event"."Location" IS 'The location of the race';

COMMENT ON COLUMN "Race_Event"."Date" IS 'The time of the race';

COMMENT ON TABLE "Team" IS 'Contains general team information';

COMMENT ON TABLE "Shipment" IS 'The shipments contain all the containers';

COMMENT ON COLUMN "Shipment"."Method" IS 'Ship, plane, truck, submarine, etc.';

COMMENT ON COLUMN "Shipment"."CreatedBy" IS 'showes Race Event Organizer ID';

COMMENT ON TABLE "Container" IS 'Container can contain kits or f1 equipment';

COMMENT ON COLUMN "Kit"."KitSize" IS 'small, medium, large';

COMMENT ON TABLE "TeamKit_Manager" IS 'The person who manages the teams kits';

COMMENT ON TABLE "RaceCrew_Member" IS 'Inbound, on site, or Outbound as role, The person who manages the teams kits';