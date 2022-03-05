#Identifications
Addition = "add"
Subtraction = "sub"
Multiplication = "mul"
Divition = "div"
squareRoot = "sqr"

def main():
    #Info
    print("Type (add) if you use Addition, Type (sub) if you use Subtraction, Type (mul) if you use Multiplication and Type (div) if you use Divition")
    print("Type (sqr) if you use Square_Root")
    print("Example: Number (add/sub/mul/div/sqr) Second Number")
    
    #Fuctions
    solution = str(input("Solution here: "))
    num1 = float(input("Type a Number: "))
    num2 = float(input("Type a Second Number: "))

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
    #Error
    elif [solution != Addition, solution != Subtraction, solution != Multiplication, solution != Divition] or [num1 and num2 != float() or int()]:
        print("Math Error")
    win = str(input("Press Enter to Reload"))  
    if win is str(): 
        main()
    else:
        exit()


main()
