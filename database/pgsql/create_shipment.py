import csv
import random
import psycopg

def main():
	temp_info = []
	with open('raceEvent.csv', mode ='r')as file:
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
		temp.append(getRandomTransport())

		# created by
		temp.append(int(line[3]))

		# apply status
		temp.append(getStatus())

		# appends temp list to final_info list
		print(temp)
		cur.execute('INSERT INTO "Shipment" VALUES (%s , %s , %s, %s, %s, %s, %s)', temp)
	
	con.commit()
		

def getStatus():
	return random.choice(["Arrived", "In Transit", "Not Left"])


def getRandomTransport():
	trans = ["airplane", "truck", "boat", "submarine"]
	return random.choice(trans)

if __name__ == "__main__":
  main()