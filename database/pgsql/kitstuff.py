from faker import Faker
import csv
import faker
import psycopg
import random

NUM_TEAMS = 10
MAX_SMALL = 4
MAX_MEDIUM = 6
MAX_LARGE = 8
MAX_CON = 6010
sizes = ("small", "medium", "large")

def main():
    car_parts = [
    ("Front wing/nose assembly", "Aerodynamic component on the front of the car for downforce"),
    ("Monocoque", "Main structural part of the car for driver safety and rigidity"),
    ("Mirrors", "Provides the driver with rear visibility"),
    ("Throttles", "Controls engine power via air and fuel intake"),
    ("Paddles for clutch", "Allows gear shifts on the steering wheel without a clutch pedal"),
    ("Driver seat assembly", "Customized seat for driver comfort and safety"),
    ("Driver pedals", "Control accelerator, brake, and clutch functions"),
    ("Engine cover", "Protects the engine and reduces drag"),
    ("Cooling intake pods", "Directs air to cool engine and other systems"),
    ("Rear view mirrors", "Helps the driver see behind the car"),
    ("Top cover", "Aerodynamic panel covering the top of the car"),
    ("Lower front wishbone", "Suspension component to control wheel movement"),
    ("Engine air intake", "Provides air to the engine for combustion"),
    ("Steering wheel", "Driver's control for steering, gears, and settings"),
    ("Rear wing", "Provides rear downforce for stability"),
    ("Clutch lever", "Controls clutch engagement for gear changes"),
    ("Rear view camera", "Additional rear visibility for the driver"),
    ("Fuel tank", "Holds fuel for the engine"),
    ("Top body assembly", "Aerodynamic body panels on the car's top"),
    ("Radio", "Allows driver communication with the pit crew"),
    ("Rear suspension damper", "Controls rear suspension movements"),
    ("Front suspension damper", "Controls front suspension movements"),
    ("Steering rod", "Connects steering wheel to the wheels"),
    ("Front pushrod", "Links suspension components for front wheels"),
    ("Rear pushrod", "Links suspension components for rear wheels"),
    ("Nose wing", "Front downforce component similar to front wing"),
    ("Side wings", "Aerodynamic elements on the sides for stability"),
    ("Rear brake ducts", "Directs air to cool rear brakes"),
    ("Rear brake caliper", "Holds brake pads to apply braking force"),
    ("Tires with Bridgestone", "Rubber tires providing grip on track"),
    ("Brake discs", "Components that brake pads clamp for stopping power"),
    ("Sidepod", "Houses radiators and electronic components"),
    ("Radiator assembly", "Cools engine and transmission systems"),
    ("Engine oil tank", "Stores oil for engine lubrication"),
    ("Air filter", "Filters air entering the engine"),
    ("Rear roll bar", "Stabilizes the car’s rear end"),
    ("Engine cylinders", "Combustion chambers for engine power generation"),
    ("Exhaust manifold with diffuser", "Directs exhaust gases and aids aerodynamics"),
    ("Rear axle", "Connects rear wheels for power transmission"),
    ("Steering power", "Assists driver in steering effort"),
    ("Battery", "Supplies power to electrical systems"),
    ("Gearbox", "Houses gears to control speed and torque"),
    ("Throttle and brake pedal assembly", "Controls acceleration and braking"),
    ("Front brake ducts", "Directs air to cool front brakes"),
    ("Front brake caliper", "Holds front brake pads"),
    ("Seat belts", "Secures the driver in place for safety"),
    ("Front roll bar", "Stabilizes the car’s front end"),
    ("Electronic control", "Manages various electronic systems"),
    ("Fuel pumps", "Supplies fuel from the tank to the engine"),
    ("Fuel injectors", "Delivers fuel into engine cylinders"),
    ("Electronic injection assembly", "Controls fuel delivery to the engine"),
    ("Coolant", "Liquid for cooling engine and components"),
    ("Transmission shaft", "Transfers power from engine to wheels"),
    ("Transmission cover", "Protects transmission components"),
    ("Heat exchanger", "Transfers heat from one fluid to another"),
    ("Coolant for engine cylinder", "Specifically cools engine cylinders"),
    ("Clutch assembly", "Engages and disengages the transmission"),
    ("Turbo", "Increases engine power by forcing air into combustion"),
    ("Crankshaft", "Converts piston movement into rotational motion"),
    ("Gear ratio", "Determines output speed relative to engine speed"),
    ("Exhaust exit", "Final point where exhaust gases are expelled")
    ]

    con = psycopg.connect(host="localhost", user="dr", dbname="dr")
    cur = con.cursor()

    all_kits = []
    all_parts = []
    kit_to_container= []
    kit_id = 7000
    team_id = 1
    curr_container_id = 6000
    part_id = 10000

    while curr_container_id <= MAX_CON:
        # car_parts[random.randint(0, len(car_parts) - 1)]
        if team_id > 10:
            team_id = 1
        cur_size = sizes[random.randint(0, len(sizes) - 1)]
        total_weight = 0
        stuff = []
        if cur_size == "small":
            total_weight, stuff, part_id = getSmall(car_parts, kit_id, part_id)
        elif cur_size == "medium":
            total_weight, stuff, part_id = getMedium(car_parts, kit_id, part_id)
        else:
            total_weight, stuff, part_id = getLarge(car_parts, kit_id, part_id)
        
        this_kit = (kit_id, random.randint(0, 100), True, team_id, total_weight, cur_size)
        con.execute('INSERT INTO "Kit" VALUES (%s, %s, %s, %s, %s, %s)', this_kit)
        con.commit()
        for s in stuff:
            con.execute('INSERT INTO "KitContents" VALUES (%s, %s, %s, %s, %s)', s)
            con.commit()
            
        
        kit_id += 1
        curr_container_id += 1
        team_id += 1
        owner_id = random.randint(0, 100)

        
    
def getSmall(car_parts, kit_id, part_id):
    part_one = car_parts[random.randint(0, len(car_parts) - 1)]
    part_two = car_parts[random.randint(0, len(car_parts) - 1)]
    part_three = car_parts[random.randint(0, len(car_parts) - 1)]
    while part_one == part_two == part_three:
        part_one = car_parts[random.randint(0, len(car_parts) - 1)]
        part_two = car_parts[random.randint(0, len(car_parts) - 1)]
        part_three = car_parts[random.randint(0, len(car_parts) - 1)]
    weight_one = random.randint(10, 25)
    weight_two = random.randint(10, 25)
    weight_three = random.randint(10, 25)

    total_weight = weight_one + weight_two + weight_three
    c1 = (kit_id, part_id, part_one[0], part_one[1], weight_one)
    part_id += 1
    c2 = (kit_id, part_id, part_two[0], part_two[1], weight_two)
    part_id += 1
    c3 = (kit_id, part_id, part_three[0], part_three[1], weight_three)
    part_id += 1
    
    stuff = []
    stuff.append(c1)
    stuff.append(c2)
    stuff.append(c3)
    return total_weight, stuff, part_id
    
def getMedium(car_parts, kit_id, part_id):
    part_one = car_parts[random.randint(0, len(car_parts) - 1)]
    part_two = car_parts[random.randint(0, len(car_parts) - 1)]
    while part_one == part_two:
        part_one = car_parts[random.randint(0, len(car_parts) - 1)]
        part_two = car_parts[random.randint(0, len(car_parts) - 1)]
    weight_one = random.randint(10, 25)
    weight_two = random.randint(35, 50)
    
    total_weight = weight_one + weight_two
    c1 = (kit_id, part_id, part_one[0], part_two[1], weight_one)
    part_id += 1
    c2 = (kit_id, part_id, part_two[0], part_two[1], weight_two)
    part_id += 1
    stuff = []
    stuff.append(c1)
    stuff.append(c2)

    return total_weight, stuff, part_id

def getLarge(car_parts, kit_id, part_id):
    part_one = car_parts[random.randint(0, len(car_parts) - 1)]
    weight = random.randint(65, 75)
    stuff = []
    c1 = (kit_id, part_id, part_one[0], part_one[1], weight)
    part_id += 1
    stuff.append(c1)
    return weight, stuff, part_id
    
    

if __name__ == "__main__":
    main()
