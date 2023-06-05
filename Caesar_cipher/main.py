from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(direction, text, shift):                       
    if direction == "decode":                                       #function to encrypt/decrypt
        shift *= -1

    output = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)                            #determining the position of char in alphabet list --> list_name.index(element)
            new_index = index + shift
            output += alphabet[new_index]
        else:                                                       #special symbols/ digits/ whitespaces
            output += char
    print(f"The {direction}d code is {output}")



exit_prog = False
while not exit_prog:
    direction = input("Type encode to encrypt or decode to decrypt: ")
    text = input(f"Enter the text to {direction}: ")
    shift = int(input("Enter the shift amount: "))
    shift %= 26                                                      #to avoid outOfRange error
    

    caesar(direction, text, shift)
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    x = input("Do you want to continue ciphering(y/n): ").lower()
    if x == "n":
        exit_prog = True
        print("Goodbye")


