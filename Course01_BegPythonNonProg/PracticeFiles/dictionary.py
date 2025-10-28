cats = {
    "Jane": 6,
    "Tom": 14,
    "Sara": 8
}

#same as:
#cats = {"Jane": 6, "Tom": 14, "Sara": 8}

#add new value to dictionary
cats["Wilson"] = 1

#delte from dictionary
del(cats["Jane"])

print(len(cats))
#get specific item from dictionary
#use key to get value/definition of key
print(cats["Tom"])

print(cats)


#challenge: 
#create dictionary with ints for keys and Booleans for values

challenge = {
    1: True,
    2: False
}
print(challenge)