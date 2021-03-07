d = {
    "roll_no":" 98",  
    "Name":"Chaitanya",
    "Marks":"  99"
}

d["roll_no"] = int(d.get("roll_no"))

d["Marks"] = int(d.get("Marks"))

print(d)

v = d.pop("roll_no")

print(v)

d.popitem()
print(d)