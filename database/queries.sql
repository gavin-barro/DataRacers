Table Race_Event {
  RaceID int [pk, not null, note: 'The current race'] 
  Location Text [not null, note: 'The location of the race']
  Date dateTime [not null, note: 'The time of the race']

  note: 'This table contains general information about the race'
}


Table Team {
  TeamID int [pk, not null]
  RaceID int [not null]
  TeamName text [not null]

  Note: 'Contains general team information'
}

Table Shipment {
  ShipmentID int [pk, not null]
  RaceID int [not null]
  CurrentLocation Text [not null]
  Destination Text [not null]
  Method text [note: 'Ship, plane, truck, submarine, etc.']

  Note: 'The shipments contain all the containers'
}

Table Container {
  ConID int [pk, not null]
  ShipmentID int [not null]
  CriticalContainer boolean [not null]

  Note: 'Container can contain kits or f1 equipment'
}

Table Container_contains_Kits {
  ConID int [not null]
  KitID int [not null]
}

Table Race_Kit {
  KitID int [pk, not null]

  Note: 'Contains f1 equipment'
}

Table Team_Kit {
  KitID int [not null]
  TeamID int [not null]

  Note: 'Contains individual team equipment'
}


Ref: Race_Event.RaceID < Team.RaceID
Ref: Container.ConID < Container_contains_Kits.ConID
Ref: Container_contains_Kits.KitID - Team_Kit.KitID
Ref: Shipment.ShipmentID < Container.ShipmentID
Ref: Race_Event.RaceID < Shipment.RaceID
Ref: Team.TeamID < Team_Kit.TeamID
Ref: Container_contains_Kits.KitID < Race_Kit.KitID
