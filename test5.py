string = []

string = (input("Enter a string: "))
print("inverted characters: ")

for i in range(len(string), 0, -1):
    print(string[i-1], end=' ')
