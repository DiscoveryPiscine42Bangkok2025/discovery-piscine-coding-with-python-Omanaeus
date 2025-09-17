print("Start talking to me! Type 'STOP' to end.")
    
    
while True:
        
    user_input = input("What you gotta say?: ")    
    if user_input.upper() == "STOP":
        print("Okay, goodbye!")
        break  # Exit the loop
    else:
        print(f"I got that! Anything else? : {user_input}")