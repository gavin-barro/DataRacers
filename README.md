# CS374 Database Project Proposal

Project Title: **Formula One Logistical Database (F1LDB)**

Team Name: **Data Racers**

Short Name: **DR**

Team Members: **Stella Lee, Kane Dacier, Gavin Barro, Austin Earl**

# Introduction

**Formula One (F1)** is the highest level of motorsport, featuring open-wheel, single seater cars that race at high speeds on circuits across the world. Governed by the Fédération Internationale de l'Automobile (FIA), F1 is renowned for its combination of cutting-edge engineering, driver skills, and team strategy. Teams design their cars with strict regulations, focusing on aerodynamics, tire management, and power units. Races, known as Grand Prixs, take place on diverse tracks ranging from purpose built courses to street circuits. Drivers accumulate points throughout the season, with championships awarded for both drivers and teams based on overall performance.

We propose to develop the “Formula 1 Logistical Database (F1LDB)” which is the central location for Race Organizers, Team Managers, and Crew Members to keep track of the large amounts of equipment that will trot the globe during the Formula 1 season. F1LDB will allow Race Organizers to add Formula 1 races to the calendar and schedule the shipping of the equipment between races. Team Managers can manage the status of their equipment as it is loaded and unloaded and select how it will be shipped. Race Crew Members manage the equipment and supplies owned by the league (broadcasting equipment etc) and are able to log on and keep track of the equipment.

# Primary System Entities

| SYSTEM ENTITY | ATTRIBUTES |
| :---- | :---- |
|  Race Event | Race Name, Date of Race, Teams Involved name, description, advertisement, size, space and tools requirements, etc. |
| Kits | Team of Kit, Size, Number of Containers(it takes up), description |
| Containers | Team Name, Critical Container, Method of shipment, Current Location, Destination |

The F1LDB simplifies tracking of equipment by having a cohesive database that displays location and shipping information. With this, teams can efficiently determine which equipment needs to be shipped for current/future races. Historical data on previous races can also be incorporated for reference for the users of the system which can help improve planning for future races.

Race Events are individual F1 Races. Each season features about 20 races occurring every week or two. The Team Kits are the equipment owned by each individual team. They have the tires, mechanics equipment, uniforms etc. Our system does not care about the contents of each kit, that is for each team to manage at their own level. Containers are the equipment owned by the F1 League and contain the necessary equipment to run each race.

# Primary System Users

| USER GROUP | ACTIVITIES & PERMISSIONS |
| :---- | :---- |
| Race Event Organizer | Race Event Organizers are in charge of an individual race. They create races as well as schedule the shipments to and from the race location |
| Team Manager | Team managers can manage the equipment(kit) of their individual team. They input the system when the equipment is loaded and unloaded, and when containers are shipped to their destination |
| Race Crew Members  | Race crew members manage the equipment owned by the race organizer. They keep the status of the equipment up to date in the database. |

Race Event Organizers are the highest level of authority in the database. Their primary role is to schedule races in the system, as well as the shipping of equipment to and from the race location. Team Managers are the point of contact for each team. They tell the database when their team's equipment is loaded and unloaded from shipping. They also select which shipment to use to ship their team kit. Race Crew Members are in charge of the equipment owned by the F1 League, such as broadcasting equipment, officiating equipment, etc. They tell the database when the equipment is loaded and unloaded.

# System Functionality

## Kits and Containers

* The kits are maintained by the teams and containers are maintained by the crew.
* The kits contain the car, replacement car parts, communication equipment, and other miscellaneous equipment.
* The containers contain the kits and the other equipment owned by the Formula One league.
* The containers are marked as critical and non-critical, the critical equipment will arrive before the non-critical equipment will.

## Crew Members and Team Managers (separate)

* Crew Members and Team Managers load and unload the equipment from shipping.
* Crew Members select the shipping method based on the location of the next event.
* Crew Members can add new shipping containers to the system.
* Inbound Crew members unload containers, and packup crew members load containers
* Crew Members assign a Race Event an instance of Non-Critical Equipment
* Race Organizers schedule Races and select the current race in the system.
* Race Crew Members schedule planes, trucks, and ships for shipping.

# About the Team

**Kane Dacier** is a Junior Computer Science student at James Madison University. He is originally from Williamsburg, VA and loves to spend his free time on long runs around Harrisonburg and watching football, particularly the Dukes and the Pittsburgh Steelers. He also loves to hike and camp, frequently combining the two activities into backpacking trips around the Blue Ridge Mountains.

**Gavin Barro** is a Senior Computer Science major and Data Analytics minor at James Madison University. He is from Clinton, NJ and enjoys running track and spending free time with friends, whether that is watching various sports indoors or hanging out outdoors. He will be attending Virginia Tech in the fall of 2025 for graduate school.

**Austin Earl** is a Senior Computer Science Major and Data Analytics minor at James Madison University. He is originally from Annapolis Maryland. He enjoys spending his free time playing video games, hanging out with friends, playing golf, and going to breweries. He will be graduating in December of 2025 and hopefully be working after he graduates.

**Stella Lee** is a Senior Computer Science Student at James Madison University. She is from Fairfax City, in Northern Virginia. She enjoys the data/ML/research side of computer science and would like to pursue an interdisciplinary education that combines CS and sciences. She spends time with her friends and her cat as much as possible. Otherwise, she is found drawing/journaling or reading books outside in her spare time.
