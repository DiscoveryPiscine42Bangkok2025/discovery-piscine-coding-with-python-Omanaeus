number = int(input("Enter a number: "))
        
print(f"Multiplication table for {number}:")
        
if number >= 0 :       
    for i in range(10):
            result = i * number
            print(f"{i} x {number} = {result}")
else :       
    print("Invalid input. Please enter a valid number.")