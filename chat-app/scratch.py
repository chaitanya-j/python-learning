dict1 = {
    "Chaitanya": 98.5,
    "Vishrut":98.4,
    "Neel": 95,
    "Samarth": 93,
    "Vardhan":90,
    "Adwait":96,

    
}
sorted_values = sorted(dict1.values(),reverse=True) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]
            break

print(sorted_dict)