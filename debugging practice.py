print("Welcome to the Temperature converter!")
print("This program converts between CElsius and Fahrenheit.")

continue_program = "yes"

while continue_program == "yes":
    temperature = int(input("Enter the temperature"))
    conversion = input("Convert to (C)elsius or (F)ahrenhiet")

    if conversion == "C":
        result = (temperature - 32) * 5/9
        original_unit = "Fahrenheit"
        converted_unit = "Celsius"
        print(result)
    elif conversion == "F":
        result = (temperature * 9/5) + 32
        original_unit = "Celsius"
        converted_unit = "Fahrenheit"
        print(result)

    else:
        print("invalid conversion choice")

    continue_program = input("do you want to continue yes/no")
