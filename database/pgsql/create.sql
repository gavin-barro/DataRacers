CREATE TABLE "Race_Event" (
  "RaceID" int UNIQUE PRIMARY KEY NOT NULL,
  "Location" Text NOT NULL,
  "Date" date NOT NULL,
  "Creator" int NOT NULL
);

CREATE TABLE "Team" (
  "TeamID" int UNIQUE PRIMARY KEY NOT NULL,
  "RaceID" int NOT NULL,
  "TeamName" text NOT NULL
);

CREATE TABLE "Shipment" (
  "ShipmentID" int UNIQUE PRIMARY KEY NOT NULL,
  "RaceID" int NOT NULL,
  "CurrentLocation" Text NOT NULL,
  "Destination" Text NOT NULL,
  "Method" text,
  "CreatedBy" int NOT NULL,
  "Status" text NOT NULL
);

CREATE TABLE "Container" (
  "ConID" int UNIQUE PRIMARY KEY NOT NULL,
  "ShipmentID" int NOT NULL,
  "CriticalContainer" boolean NOT NULL,
  "Status" text NOT NULL,
  "UpdatedBy" int NOT NULL
);

CREATE TABLE "ContainerContents" (
  "ConID" int UNIQUE NOT NULL,
  "KitID" int NOT NULL,
  PRIMARY KEY ("ConID", "KitID")
);

CREATE TABLE "Kit" (
  "KitID" int UNIQUE NOT NULL,
  "OwnerID" int NOT NULL,
  "TypeOfKit" boolean NOT NULL,
  "TeamID" int NOT NULL,
  "TotalWeight" int NOT NULL,
  "KitSize" text,
  PRIMARY KEY ("KitID", "OwnerID")
);

CREATE TABLE "Race_Event_Organizer" (
  "OrganizerID" int UNIQUE PRIMARY KEY NOT NULL,
  "Name" text NOT NULL,
  "Permisions" text NOT NULL
);

CREATE TABLE "Person" (
  "PersonID" int UNIQUE PRIMARY KEY NOT NULL,
  "Name" text NOT NULL,
  "KitID" int NOT NULL,
  "PhoneNum" text NOT NULL,
  "Permisions" text NOT NULL
);

CREATE TABLE "TeamKit_Manager" (
  "PersonID" int UNIQUE PRIMARY KEY NOT NULL,
  "TeamID" int NOT NULL
);

CREATE TABLE "RaceCrew_Member" (
  "PersonID" int UNIQUE PRIMARY KEY NOT NULL,
  "Role" text NOT NULL
);

CREATE TABLE "KitContents" (
  "KitID" int NOT NULL,
  "PartID" int UNIQUE PRIMARY KEY NOT NULL,
  "PartName" text NOT NULL,
  "PartDesc" text NOT NULL,
  "PartWeight" int NOT NULL
);