from faker import Faker
import csv
import faker
import psycopg
import random

NUM_PEOPLE = 100 # Number of people
STARTING_PID = 1 # Initial value of PersonID, IDs will increment incrementally from here
STARTING_KID = 1 # Initial Value of Kit ID
NUM_TEAMS = 10 # number of teams
NUM_KITS = 10
MAX_KIT_WEIGHT = 1000
NUM_CONT = 10 # number of containers
MAX_KITS_CONTAINED = 5 # max number of kits in a container (can change this later)
MAX_PART_WEIGHT = 20
MAX_KIT_CONTENTS = 10


# Set of permissions for Persons. We can change this as needed
permissions = ["all", "change_kits", "change_containers", "change_shipping"]


# Connect to Database
con = psycopg.connect(host="localhost", user="dr", dbname="dr")
cur = con.cursor()

# Initialize generators
random.seed(0)
fake = faker.Faker()


def main():
    locales = ['it_IT', 'fr_FR', 'de_DE', 'es_ES', 'nl_NL', 'pl_PL']
    euro_fake = Faker(locales)
    
    european_names = [euro_fake.name() for _ in range(50)]

    # Generate fake people
    persons = []
    j = STARTING_PID
    for _ in range(NUM_PEOPLE):
        person = (
            j,
            euro_fake.name(),
            0, # Kit ID, Remove when we remove Kit ID from the person Table
            euro_fake.phone_number(),
            permissions[random.randint(0, 2)]
        )
        j+=1
        #cur.execute('INSERT INTO "Person" VALUES (%s, %s, %s, %s, %s)', person)
    #con.commit()

    # Generate Team Kit Managers
    x = 1
    for i in range(1, NUM_TEAMS + 1):
        person = (x, i)
        #cur.execute('INSERT INTO "TeamKit_Manager" VALUES(%s, %s)', person)
        x += 1
    #con.commit()

    # Generate Kits
    starting_kit_id = 5000
    sizes = ("small", "medium", "large")
    for i in range(0, NUM_KITS):
        kit = (
            starting_kit_id + i,
            #random.randint(0, NUM_PEOPLE), # OwnerID
            i + 1,
            random.choice([True, False]),   
            random.randint(1, 10),         # Team ID
            random.randint(1, MAX_KIT_WEIGHT),
            sizes[random.randint(0, 2)]
        )
        #cur.execute('INSERT INTO "Kit" VALUES(%s, %s, %s, %s, %s, %s)', kit)
    # generate containers with kit(s) in them
    con.commit()
    for i in range(NUM_CONT):
        kits_contained = random.randint(1, MAX_KITS_CONTAINED)
        for j in range(kits_contained):
            temp = []
            temp.append(i)
            temp.append(starting_kit_id)
            #cur.execute('INSERT INTO "ContainerContents" VALUES (%s, %s)', temp)
            starting_kit_id += 1
    #con.commit()
    # someone run this when containers is put into database
    
    starting_kit_id = 5000
    container_id = 6001

    for i in range(NUM_CONT):
        temp = [starting_kit_id, starting_kit_id]
        #cur.execute('INSERT INTO "ContainerContents" VALUES (%s, %s)', temp)
        starting_kit_id += 1
        container_id += 1
        
    #con.commit()
    
    #Generate KitContents
    starting_part_id = 50
    for i in range(5000, 5010):

        temp = (
            i,
            random.randint(1, 100),
            euro_fake.bs(),
            random.randint(1, MAX_PART_WEIGHT)
        )
        cur.execute('INSERT INTO "KitContents" VALUES (%s, %s, %s, %s)', temp)
    con.commit()
if __name__ == "__main__":
    main()