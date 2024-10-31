import csv
import random
import psycopg

num_containers = 10
num_shipments = 46

def main():
	temp_info = []
	with open('../data/raceEvent.csv', mode ='r')as file:
		csvFile = csv.reader(file)
		for lines in csvFile:
			temp_info.append(lines)
	
	final_info = []
	curr_id = 5000
	prev_location = ""
	temp_info.pop(0)
	
	con = psycopg.connect(host="localhost", user="dr", dbname="dr")
	cur = con.cursor()

	for line in temp_info:
		temp = []
		# gets shipment id
		temp.append(curr_id)
		curr_id += 1

		# gets race id
		temp.append(int(line[0]))

		# sets current and new destination
		if len(prev_location) == 0:
			temp.append("Store House")
			temp.append(line[1])
			prev_location = line[1]
		else:
			temp.append(prev_location)
			temp.append(line[1])
			prev_location = line[1]
		
		# applies random transportation
		temp.append(get_random_transport())

		# created by
		temp.append(int(line[3]))

		# apply status
		temp.append(get_status())

		# appends temp list to final_info list
		cur.execute('INSERT INTO "Shipment" VALUES (%s , %s , %s, %s, %s, %s, %s)', temp)
	
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
		
def get_rand_boolean():
	return random.choice([True, False])

def get_status():
	return random.choice(["Arrived", "In Transit", "Not Left"])

def get_random_transport():
	trans = ["airplane", "truck", "boat", "submarine"]
	return random.choice(trans)


if __name__ == "__main__":
  main()