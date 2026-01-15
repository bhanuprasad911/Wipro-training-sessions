import xml.etree.ElementTree as et
tree = et.parse("day3/Students.xml")
root = tree.getroot()

for student in root.findall("Student"):
    id=student.find("Id").text
    name=student.find("Name").text
    age=student.find("Age").text
    print(id, name, age)

root=et.Element("employee")
emp1=et.SubElement(root,"emp")
et.SubElement(emp1,"id").text="101"
et.SubElement(emp1,"Name").text="Rama"
et.SubElement(emp1,"Salary").text="100000"
emp2=et.SubElement(root,"emp")
et.SubElement(emp2,"id").text="102"
et.SubElement(emp2,"Name").text="pavi"
et.SubElement(emp2,"Salary").text="200000"

tree=et.ElementTree(root)
tree.write("employee.xml")
print("xml file written successfully")

    