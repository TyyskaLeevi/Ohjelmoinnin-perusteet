children = 3
hometown = "lahti"

# lista
townsinfinland = ["lahti", "helsinki", "lappeenranta", "oulu", "tampere"]

randominfo = ["mira", 48, True, children, hometown]

print(townsinfinland[0])
townsinfinland.append("rovaniemi")
print(townsinfinland)

numoftowns = len(townsinfinland)
print(townsinfinland[numoftowns-1])

municipalities = ["asikkala", "hollola", "karvia", "kempele"]
towns = ["lahti", "helsinki", "lappeenranta", "oulu", "tampere"]

municipalitiesandtowns = [municipalities, towns]

print(municipalitiesandtowns[1][-2])

towns.sort()
print(towns)

teacher = {
    'name': 'juha',
    'age': '50',
    'city': 'lahti'
}

print(teacher["name"])

teacher['email']= 'juha.hyytiainen@lab.fi'

print(teacher)

for key in teacher:
    print(key, end=' ')
    print(teacher[key])

student = [
    {'name': 'mikko', 'age': 25, 'city': 'tampere'},
    {'name': 'miaja', 'age': 30, 'city': 'espoo'},
    {'name': 'seppo', 'age': 35, 'city': 'helsinki'}
]
print(student[0])

cities = {
    'finland':['tampere', 'espoo', 'helsinki'],
    'sweden':['stockholm', 'malmö'],
}
print(cities['finland'][0])

for town in towns:
    print(f"the town of {town}")
print(f"all of the towns {towns}")