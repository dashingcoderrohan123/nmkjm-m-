def decimal_to_binary(decimal):
    binary = ''
    
    # Handle the case for zero
    if decimal == 0:
        return '0'
    
    # Keep dividing the number by 2 and storing the remainder
    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary
        decimal = decimal // 2
    
    return binary

# Taking user input
decimal_number = int(input("Enter a decimal number: "))

# Convert to binary
binary_number = decimal_to_binary(decimal_number)

# Display the result
print(f"The binary equivalent of {decimal_number} is {binary_number}")
