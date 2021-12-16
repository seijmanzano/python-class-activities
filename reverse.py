def reverse(text):
    y = str.upper(text)
    x = y[::-1]
    print("Reversed String: ", x, "String Length: ", len(text))


text = input("Enter the string to be reversed: ")
reverse(text)
