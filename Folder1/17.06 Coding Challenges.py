# 	• Create variables to store one pet's information: name, type (dog/cat/bird), age, and vaccination status (true/false)
# 	• Ask the user to input a pet's name and display a welcome message
# Use an if statement to check if the pet is under 1 year old and display "This is a baby pet!"
name = input("what is your pets name? ")
print(f"Welcome {name}")
age = int(input("what is your pets age? "))
vaccination = bool(input("Are they vaccinaate? "))
print(vaccination)
if age <= 1:
    print("Is a baby")
