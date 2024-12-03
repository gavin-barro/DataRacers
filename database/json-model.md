# Document Database Model

Project Title: **F1DB**

Team Name: **dr**


## Relational Mapping

The following **4 collections** correspond to the **12 tables** found in [schema.png](schema.png).

* Race Event
    * raceid
    * location
    * date

* Team
    * team
    * raceevent

* Person
    * room
    * room_feature
    * feature

* Kit
    * container_id

* Shipment
    * shipment_id
    * current_location
    * destination
    * method
    * created_by
    * status

* Container
    * ConID
    * ShipmentID
    * CriticalContainer
    * Status
    * UpdatedBy

* Kit
    * KitID
    * OwnerID
    * TypeOfKit
    * TeamID
    * TotalWeight
    * KitSize

* KitContents
    * KitID
    * PartID
    * PartName
    * PartDesc
    * PartWeight


## The Race Event Collection

The location, date, and creator are stored in the Race Event Collection. Since race events are usually created in advance, the location and date are predetermined and don't often change (except in rare circumstances). The Creator of the race does not change. 
A link (dbms specific) is stored to the person who created the event (race event organizer). This is linked with our Person collection.

```
{
    'raceid': '322',
    'location': 'Canada',
    'official_name': '2024 Canadian Grand Prix'
    'date': '03-24-2024',
    'creator': {
        'id': '10',              # DBMS-specific linking
        'name': 'Frances Baguette',
    }
}
```


## The Shipment Collection

The Shipment Collection stores information about the transportation of containers for a race event. Each shipment includes its current location, destination, and method of transport, which may vary depending on logistical needs. Shipments are linked to the race they support and are created by an organizer, with a (DBMS specific) link to the Person Collection. Containers within the shipment, including critical status and their contents, are nested for easy tracking and management.

```
{
    "shipmentid": "5002",
    "raceid": "1100",
    "currentlocation": "Saudian Arabian Grand Prix",
    "destination": "Australian Grand Prix",
    "method": "Submarine",
    "createdby": {
        "id": "10",  # DBMS specific linking
        "name": "Dragan Scholl"
    },
    "status": "Arrived",
    "containers": [
        {
            "conid": "6020",
            "critical": True,
            "status": "Submarine",
            "updatedby": {
                "id": "14",  # DBMS specific linking
                "name": "Chloë Hemma van Allemanië"
            }
        }
    ]
}

```

## The Container collection

```
{
    "ConID": "6000",
    "ShipmentID": "5000",
    "CriticalContainer": "True",
    "Status": "Submarine",
    "method": "In-Transit",
    "UpdatedBy": 0
}
```


## Kit
```
{
    "KitID": "7000",
    "OwnerID": "2",
    "TeamID": "1",
    "TotalWeight": "71",
    "KitSize": "large"
}
```

## KitContents
```
{
    "KitID": "7000",
    "PartID": "1000",
    "PartName": "Transmission Cover",
    "PartDesc": "Protects transmission components",
    "PartWeight": "71"
}
```



## The Room Collection

The room, department, and college data could be stored in their own collections to serve as lookup tables, but they hardly change and could be managed some other way.
The timeslot data for the day's schedule also may or may not be stored in a collection.
Room is shown as an example collection below.

```
{
    'name': 'ENGEO 2204',
    'type': 'computer lab',
    'capacity': 32,
    'features': [
        {
            'name': 'lab',
            'description': '32 Linux Mint desktops',
        },
        {
            'name': 'instructor computer',
            'description': '1 Linux Mint desktop',
        },
        {
            'name': 'projector',
            'description': 'connection from instructor computer or HDMI',
        },
    ]
}
```


## The Event Collection

Finally, each event stores the date and the conference organizers.
The year is stored separately (and redundant), given the year is used in so many instances in the application.

```
{
    'id': 5,
    'year': 2024,
    'date': '2024-03-23',
    'organizers': [
        {
            'person': 'lam2mo',       # DBMS-specific linking mechanism
            'roles': ['co-chairperson', 'volunteer team'],
        },
        {
            'person': 'elkadima',       # DBMS-specific linking mechanism
            'roles': ['workshop team'],
        },
    ]
}
```
