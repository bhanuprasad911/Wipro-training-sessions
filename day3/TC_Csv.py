import csv
with open ("Student.csv", 'w', newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Id", "Name", "Age"])
    writer.writerow(["01", "Bhanu", "22"])
    writer.writerow(["02", "Vamshi", "23"])
    writer.writerow(["03", "Srujan", "24"])
    
    
    