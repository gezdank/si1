while True:
    num_1 = (input("Enter a number: "))
    
    if num_1.isdigit() != True:
        print()
        break
    else:
        num_2 = (input("Enter a second number: "))
        op = input("Enter an operator: ")
        if op == "+":
            print(int(num_1) + int(num_2))
        elif op == "-":
            print(int(num_1) - int(num_2))
        elif op == "*":
            print(int(num_1) * int(num_2))
        elif op == "/":
            print(int(num_1) / int(num_2))
        else:
            print("invalid operator") 
         
