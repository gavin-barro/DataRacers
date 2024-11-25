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
    * 


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


## The Workshop Collection

The room name can be stored directly in the workshop.
The list of rooms, including department and college information, hardly changes and may not even need to be stored---it's just used for lookup.
The list of people involved can just be minimal, but this duplication may be helpful.
A link to the full Person data is not required from this direction, but may be stored anyway.

```
{
    'id': 299,
    'state': 'accepted',
    'title': 'Create your own game!',
    'advertisement': 'Create your own game using Scratch...',
    'description': 'Students will use Scratch to develop a fish game...',
    'capacity': 15,
    'computer_needs': 'Each student needs a computer.',
    'room_needs': 'Computer lab is best, or laptops',
    'max_repeat': 3
    'parent_questions': 'Ask you child to show your their game on the Scratch site.',
    'other_information': 'N/A',
    'event_year': 2023,
    'room_name': 'ENGEO 2204',
    'timeslots': [
        {
            'start': '9:30',
            'end': '10:30',
        },
        {
            'start': '13:20',
            'end': '13:40',
        }
    ]
    people: [
        {
            'name': 'Mona Rizvi',
            'phone': '17571111111',
            'role': 'lead',
            'id': 'elkadima',    # DBMS-specific linking mechanism
        },
        {
            'name': 'Mariya Rizvi',
            'phone': '17572222222',
            'role': 'volunteer',
            'id': 'rizvi',       # DBMS-specific linking mechanism
        },
    ]
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
