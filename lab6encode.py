#Lab 6
#Author: Ezekiel Pasion

def encode(key):
    encoded = ""
    for char in key:
        number = int(char)
        number +=3
        encoded += str(number)
    return encoded

#Menu
password = ""
encoded = ""

while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    option = int(input("\nPlease enter an option: "))

    if option == 1:
        password = input("Please enter your password to encode: ")
        encoded = encode(password)
        print("Your password has been encoded and stored!")

    # elif option == 2:
    #     if password == "":
    #         print("No password stored!")
    #     else:
    #         password = decode(encoded)
    #         print ("The encoded password is " + encoded + ", and the original password is " + password + ".")

    elif option == 3:
        break
    else:
        print("Invalid option")
    print()