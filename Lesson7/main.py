# age = 25
# age_as_str = str(age)
# print(age_as_str + " type of", type(age_as_str))

# x = 12
# y = 5.3
# result = x + y
# print(type(result))
#
# message = "I am " + str(age) + " Years old"
# print(message)

# this will generate an error
# z = int("abc")

# name = input("Enter your name: ")
# print(f"Hello, {name}")
#
# nr1 = int(input("Enter your first number: "))
# nr2 = int(input("Enter your second number: "))

# print(f"Rezultati eshte {nr1 + nr2}")

# try:
#     results = 10 / 0
#     print(results, " rezultati")
# except ZeroDivisionError:
#     print("Nuk bon me pjestu me 0")

# try:
#     text = "Fjalia eshte "
#     text_to_int = int(text)
# except Exception as e:
#     print("An error occurred while parsing the data")
# else: # this is done if there are no errors
#     print('Division successfull done')
# finally: # This is activated always with or without errors
#     print("This is always running")

def calculator(number1, number2, operator):
    if operator == "+":
        print(f"Results: {number1 + number2}")
    elif operator == "-":
        print(f"Results: {number1 - number2}")
    elif operator == "*":
        print(f"Results: {number1 * number2}")
    elif operator == "/":
        print(f"Results: {number1 / number2}")
    elif operator == "%":
        print(f"Results: {number1 % number2}")
    else:
        raise ValueError

try:
    number1 = float(input("Enter the first number: "))
    operator = input("Enter the operator: ")
    number2 = float(input("Enter the second number: "))

    calculator(number1, number2, operator)
except ValueError:
    print("Invalid input or operation")

except ZeroDivisionError:
    print("You can't divide with 0")

except Exception as e:
    print("An error occurred while parsing the data")

finally:
    print("Thank You!")