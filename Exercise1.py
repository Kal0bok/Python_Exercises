print("=== BMI Calculator ===")

weight = float(input("Enter your weight in kg: "))
height_cm = float(input("Enter your height in cm: "))
height_m = height_cm / 100

bmi = weight / (height_m ** 2)
print(f"\nYour BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi < 25:
    print("Category: Normal weight")
elif 25 <= bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obesity")