# #Read 
# f = open('sample.txt', 'r')
f = open('sample.txt') # by default the mode is r
data = f.read()
# data = f.read(5) # reads first 5 characters from the file
print(data)
# print(f.readable())
f.close()

f = open('sample.txt', 'r')
print(f.readlines())
f.close()

f = open('sample.txt')
# read first line
data = f.readline() 
print(data)

# Read second line
data = f.readline() 
print(data)

# Read third line
data = f.readline() 
print(data)

# Read fourth line... and so on...
data = f.readline() 
print(data)
f.close()

# #Write
f = open('another.txt', 'w')
f.write("I am writing")
f.write(" whole day.") 
f.close()

# #Append
f = open('another.txt', 'a')
f.write("\nThis is a poem.") 
f.close()

# Using with
with open('with.txt', 'r') as f:
    a = f.read()
with open('with.txt', 'w') as f:
    a = f.write("me")
print(a)
