# #Dictionary
myDict = {
    "fast": "In a Quick Manner",
    "Ankan": "A Coder",
    "marks": [1, 2, 5],
    "anotherdict": {'Ankan': 'Player'},
    1: 2
}

print(myDict['fast'])
print(myDict['Ankan'])
myDict['Marks'] = [45, 78]
print(myDict['Marks'])
print(myDict['anotherdict']['Ankan']) #nested dictionary

Dict= dict([(1,'Geeks'), (2,'For')])  #as a pair
print("Dict",Dict)

# #Dictionary Methods
print(list(myDict.keys())) # Prints the keys of the dictionary
print(myDict.keys())
print(type(myDict.keys()))
print(myDict.values()) # Prints the keys of the dictionary 
print(myDict.items()) # Prints the (key, value) for all contents of the dictionary 
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Divya": "Friend",
    "Shubham": "Friend",
    "Ankan": "A Dancer"
}
myDict.update(updateDict) # Updates the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("Ankan")) # Prints value associated with key "ankan"
print(myDict["Ankan"]) # Prints value associated with key "ankan"

print(myDict.get("Ankan2")) # Returns None as ankan2 is not present in the dictionary
# print(myDict["ankan2"]) # throws an error as ankan2 is not present in the dictionary

favLang = {}
a = input("Enter your favorite language Shubham\n")
b = input("Enter your favorite language Ankit\n")
c = input("Enter your favorite language Sonali\n")
d = input("Enter your favorite language Harshita\n")
favLang['shubham'] = a
favLang['ankit'] = b
favLang['sonali'] = c
favLang['harshita'] = d

print(favLang)

# #Sets
p = {1, 3, 4, 5, 1}
print(type(p))
print(p)


a = {}  # This syntax will create an empty dictionary and not an empty set
print(type(a))

# An empty set can be created using the below syntax:
b = set()
print(type(b))

## Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly does not changes a set
b.add((4, 5, 6))#Tuple allowed but not list & Dictionary

## Accessing Elements
# b.add({4:5}) # Cannot add list or dictionary to sets
print(b)

print(len(b)) # Prints the length of this set
b.remove(5) # Removes 5 fromt set b
# b.remove(15) # throws an error while trying to remove 15 (which is not present in the set)
print(b)

print(b.pop()) # Removes any arbitary elements of teh set
print(b)
 
print(b.clear())
print(b) # Empties the set


s = {18, "18", 18.00} #str and int are different
print(s)