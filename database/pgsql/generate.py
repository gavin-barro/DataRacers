from faker import Faker
import csv
import faker
import psycopg
import random

NUM_PEOPLE = 100 # Number of people
STARTING_PID = 1 # Initial value of PersonID, IDs will increment incrementally from here
STARTING_KID = 1 # Initial Value of Kit ID
NUM_TEAMS = 10 # number of teams

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
        cur.execute('INSERT INTO "Person" VALUES (%s, %s, %s, %s, %s)', person)

    # Generate Team Kit Managers
    x = 1
    for i in range(1, NUM_TEAMS + 1):
        person = (x, i)
        cur.execute('INSERT INTO "TeamKit_Manager" VALUES(%s, %s)', person)
        x += 1
    con.commit()
if __name__ == "__main__":
    main()