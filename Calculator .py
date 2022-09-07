print("Select an operation to perform!")
print("1. ADD")
print("2. SUBTRACT")
print("3. DIVIDE")
print("4. MULTIPLY")
while True:
    op=int(input())
    if op == 1:
        print("Enter num1 and num2...")
        o = int(input())
        while True:
            t = int(input())
            a = (o+t)
            print("The answer is " + str(o+t))
            print("Continue?")
            r = input()
            if r == "no":
                break
            elif r == "yes":
                o = a
                continue
            break
    elif op == 2:
        print("Enter num1 and num2...")
        o = int(input())
        while True:
            t = int(input())
            a = (o-t)
            print("The answer is " + str(o-t))
            print("Continue?")
            r = input()
            if r == "no":
                break
            elif r == "yes":
                o = a
                continue
            break
        
    elif op == 3:
        print("Enter num1 and num2...")
        o = int(input())
        while True:
            t = int(input())
            a = (o*t)
            print("The answer is " + str(o*t))
            print("Continue?")
            r = input()
            if r == "no":
                break
            elif r == "yes":
                o = a
                continue
            break

    elif op == 4:
        print("Enter num1 and num2...")
        o = int(input())
        while True:
            t = int(input())
            a = (o/t)
            print("The answer is " + str(o/t))
            print("Continue?")
            r = input()
            if r == "no":
                break
            elif r == "yes":
                o = a
                continue
            break
    
    else:
        print("Invalid entry!")
        continue
        

