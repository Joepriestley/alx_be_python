num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation =input("Enter the operation (add, subtract, multiply, divide):") 

def perform_operations(num1,num2, operation):
    
    if operation == "add": 
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
        
    else :
        
        if num2 == 0:
            result ="Invalid entry"
        else:
            result = num1 / num2
    return result


resultt = perform_operations(num1, num2, operation)
print(resultt)
    
    
    
    