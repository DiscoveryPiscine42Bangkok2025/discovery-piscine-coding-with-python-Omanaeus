num1_str = input("Enter the first number: ")
number1 = float(num1_str)

num2_str = input("Enter the second number: ")
number2 = float(num2_str)

    # คำนวณผลคูณ
result = number1 * number2

    # แสดงผลการคูณ
print(f"{number1} x {number2} = {result}")

if result > 0:
        print("The result is positive.")
elif result < 0:
        print("The result is negative.")
else: # กรณีที่ result == 0
        print("The result is positive and negative.") 