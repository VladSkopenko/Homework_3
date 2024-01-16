import sys
print(sys.argv)
message = input("Enter message:")
offset = int(input("It's offset:"))
uncoded_message = ""

for i in message:
    if i.isalpha():
        if i.isupper():
            pos = ord(i) - ord("A")
            pos = (pos - offset) % 26
            new_i = chr(pos + ord("A"))
        else:
            pos = ord(i) - ord("a")
            pos = (pos - offset) % 26
            new_i = chr(pos + ord("a"))
    else:
        new_i = i 
        uncoded_message += new_i
    print(uncoded_message)
        
    