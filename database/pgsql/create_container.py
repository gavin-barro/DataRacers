import csv
import random
import psycopg

num_containers = 10
num_shipments = 46

def main():
    con = psycopg.connect(host="localhost", user="dr", dbname="dr")
    cur = con.cursor()
    
    container_id = 6000
    curr_shipid = 5000
    for i in range(num_shipments):
        for j in range(num_containers):
            temp = []
            temp.append(container_id)
            temp.append(curr_shipid)
            temp.append(get_rand_boolean())
            temp.append(get_random_transport())
            temp.append(int(random.random()))
            container_id += 1
            cur.execute('INSERT INTO "Container" VALUES (%s, %s, %s, %s, %s)', temp)

		
        curr_shipid += 1

    con.commit()
	
def get_random_transport():
	trans = ["Airplane", "Truck", "Boat", "Submarine"]
	return random.choice(trans)

def get_rand_boolean():
	return random.choice([True, False])

if __name__ == "__main__":
  main()