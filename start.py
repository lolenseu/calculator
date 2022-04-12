import os

os.system('clear')

#Identifications
Addition = "add"
Subtraction = "sub"
Multiplication = "mul"
Divition = "div"
squareRoot = "sqr"

#Info
print("Type (add) for Addition, Type (sub) for Subtraction, Type (mul) for Multiplication, and Type (div) for Divition")
print("Type (sqr) for Square_Root")
print("Example: Number (add/sub/mul/div/sqr) Second Number")

reload = True
while reload:
    #Fuctions
    def method():
        global solution
        sub_solution = input("Solution here: ").lower()
        if sub_solution == 'add' or sub_solution == 'sub' or sub_solution == 'mul' or sub_solution == 'div' or sub_solution == 'sqr':
            solution = str(sub_solution)
            pass
        elif sub_solution != str():
            print("Please Choose on the Solution!")
            method()
        else:
            print("Please Choose on the Solution!")
            method()


    method()
    no1 = False
    while not no1:
        try:
            num1 = float(input("Type a Number: "))
            if num1 == str():
                no1 = False
            else:
                no1 = True
        except:
            print("Please Type a valid Number!")
            continue

    no2 = False
    while not no2:
        try:
            num2 = float(input("Type a Second Number: "))
            if num2 == str():
                no2 = False
            else:
                no2 = True
        except:
            print("Please Type a valid Number!")
            continue
    

    #Computations
    if solution == Addition:
        print("Addition of", num1, "and", num2, "is", num1 + num2)
    elif solution == Subtraction:
        print("Subtraction of", num1, "and", num2, "is", num1 - num2)
    elif solution == Multiplication:
        print("Multiplication of", num1, "and", num2, "is", num1 * num2)
    elif solution == Divition:
        print("Divition of", num1, "and", num2, "is", num1 / num2)
    elif solution == squareRoot:
	    print("Square Root of", num1, "and", num2, "is", num1 ** num2)