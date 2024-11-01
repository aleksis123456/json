import json

data={
    "name": "Anna",
    "age": 25,
    "city": "Riga"
}

with open ("data.json", "w") as file:
    json.dump (data,file,ident=4)