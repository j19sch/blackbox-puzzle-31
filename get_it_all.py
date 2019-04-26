import csv
import requests

from itertools import product

URL = 'http://blackboxpuzzles.workroomprds.com:8002/puzzle31/'
FILE = 'puzzle31.csv'

with open(FILE, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    fieldnames = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'lamp1', 'lamp2', 'lamp3', 'lamp4']
    csv_writer.writerow(fieldnames)

    for combination in product(('up', 'down'), repeat=9):
        csv_row = list(combination)
        params = {
            "buttonA1": combination[0],
            "buttonA2": combination[1],
            "buttonA3": combination[2],
            "buttonB1": combination[3],
            "buttonB2": combination[4],
            "buttonB3": combination[5],
            "buttonC1": combination[6],
            "buttonC2": combination[7],
            "buttonC3": combination[8]
        }

        response = requests.get(URL, params=params)

        csv_row.extend(response.json().values())
        csv_writer.writerow(csv_row)
