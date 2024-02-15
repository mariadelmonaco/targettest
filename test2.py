element = int(input("Enter a integer number: "))
a, b, c = 0, 1, 0

if (element == 0):
    print(a, "\nThe element: ", element, " is in the sequence")
elif (element == 1):
    print(a, b, "\nThe element: ", element, " is in the sequence")
else:
    print(a, b, end=' ')
    for i in range(element + 1):
        if (c < element):
            c = a + b
            a = b
            b = c
            print(c, end=' ')
        elif (c == element):
            print("\nThe element: ", element, " is in the sequence")
            break
        else:
            print("\nThe element: ", element, " is not in the sequence")
            break
