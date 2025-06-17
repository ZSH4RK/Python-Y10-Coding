#debug 1
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


#debug 2
print("welcome to the number guessing game")
print("I'm thinking of a number from 1 to 100")

secret_number = 42

max_attempts = 5
attempts = 0

while attempts < max_attempts:
    attempts += 1
    print(f"Attempt {attempts} of {max_attempts}")
    guess = int(input("Enter the guess "))

    if guess == secret_number:
        print("Correct")
        break
    elif guess < secret_number:
        print("Too Low")

    else:
        print("too high")

