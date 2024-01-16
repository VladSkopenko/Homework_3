message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for i in message:
    if i.isalpha():
        if i.isupper():
            pos = ord(i) - ord("A")
            pos = (pos + offset) % 26
            new_i = chr(pos + ord("A"))
        else:
            pos = ord(i) - ord("a")
            pos = (pos + offset) % 26 
            new_i = chr(pos + ord("a"))
    else:
        new_i = i 
    encoded_message += new_i
    
print(encoded_message)