

print("======================10-1===================")

file_name = "learning_python.txt"
with open(file_name) as f:
    contents = f.read()
print(contents)

print("\n---Looping over the lines:")
with open(file_name) as f:
    for line in f:
        print(line.rstrip())

print("\n--- Storing the lines in a list:")
with open(file_name) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())

print("======================10-===================")




