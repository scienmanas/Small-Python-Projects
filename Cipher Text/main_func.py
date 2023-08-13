from Additionals import alphabet, logo

# Printing Logo

print(logo)


def encode(message, shift_number):
    index = 0
    result1 = []
    for i in range(len(message)):
        for index in range(27, 54):
            if (alphabet[index] == message[i]):
                break
        result1 += alphabet[index+shift_number]
    return result1


def decode(message, shift_number):
    index = 0
    result1 = []
    for i in range(len(message)):
        for index in range(27, 54):
            if (alphabet[index] == message[i]):
                break
        result1 += alphabet[index-shift_number]
    return result1


def final_result(work, message, shift_number):
    if (work == "encode"):
        result1 = encode(message, shift_number)
    else:
        result1 = decode(message, shift_number)
    return result1


def printing(result):
    print(''.join(result))

# Taking Inputs from user


work = input("Type 'encode' to encrpt, type 'decode' to decrypt: \n").lower()
message = input("Type Your Message:\n").lower()
shift_number = int(input("Type shift number\n"))

# Calculting and Printing

result = final_result(work, message, shift_number)
printing(result)

# Enhancing user experience

while input("Type 'yes' if you want to go again. Otherwise type 'no'. \n").lower() == "yes":
    # taking Input from the user
    work = input("Type 'encode' to encrpt, type 'decode' to decrypt: \n").lower()
    message = input("Type Your Message:\n").lower()
    shift_number = int(input("Type shift number\n"))
    # Printing and Calculation
    result = final_result(work, message, shift_number)
    printing(result)
