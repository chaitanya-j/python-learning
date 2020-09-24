# Our Dictionary.
marks = {
    "Chaitanya": 98.5,
    "Neel": 95,
    "Samarth": 93
    
}
flg = False

# Reading an entry in in marks using square bracket notation.
ch_marks = marks["Chaitanya"]

# reading an entry in marks using get method.
neel_marks = marks.get("Neel")
pan_marks = marks.get("Pankaj")

# Printing the values of.
print(f"Chaitanya scored {ch_marks} %")
print(f"Neel scored {neel_marks} %")
print(f"Pankaj scored {pan_marks} %")

# Adding a new entry in the dictionary. 
marks["Pankaj"] = 96.5

# Printing the whole dictionary.
print(marks)

marks.pop('Pankaj')
print(marks)

if 'Neel' in marks:
    flg = True

print(flg)
