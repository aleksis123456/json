import json

with open ("skoleni.json", "r" ,encoding="utf - 8") as file:
    skoleni=json.load(file)
print(skoleni)

print("Cilvēki kuriem atzīme >4 un <7 :")
print()
for person in skoleni:
    if person["atzīme"]<7:
           print(person["name"])