#Python writeing files (.txt, .json, .csv)

import json
import csv

txt_data = "I like pizza"
employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

file_path = "output.txt"


try:
    with open(file=file_path,mode= "a") as file:  # w - write,  x - wirte if dosnt exist, a - to append
        for employee in employees:
            file.write(employee + "\n")
            print(f"Data written to {file_path} was     created")
except FileExistsError:
    print(f"The file {file_path} already exists")


employee = {
    "name" : "Spongebob",
    "age" : 30,
    "job" : "Cook"
}

file_path1 = "employees.json"
try:
    with open(file=file_path1, mode="a") as file:
        json.dump(employee, file, indent=4)
        print(f"Data written to {file_path1} was created")
except FileExistsError:
    print(f"The file {file_path1} already exists")


employees1 = [["Name", "Age", "Job"],
              ["Spoungebob", 30, "Cook"],
              ["Patrick", 37, "Unemployeed"],
              ["Sandy", 27, "Scientist"]]

file_path2 = "employees.csv"

try:
    with open(file=file_path2, mode="w", newline="") as file:
        writer = csv.writer(file)
        for row in employees1:
            writer.writerow(row)
        print(f"csv file {file_path2} was created")
except FileExistsError:
    print(f"The file {file_path2} already exists")