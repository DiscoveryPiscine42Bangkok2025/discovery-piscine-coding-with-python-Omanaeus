start_num_str = input("Enter a number less than 25: ")
start_num = int(start_num_str) 

    
if start_num > 25:
        print("Error")
else:
    
    for current_num in range(start_num, 26):
            print(f"Inside the loop, my variable is {current_num}")