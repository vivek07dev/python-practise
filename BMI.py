weight = float(input("Enter your weight in kilograms: "))
feet = int(input("Enter your height (feet): "))
inches = float(input("Enter additional inches: "))

total_inches = feet * 12 + inches
height_meters = total_inches * 0.0254

if weight <= 0 or height_meters <= 0:
    print("Weight and height must be greater than zero.")
else:
    bmi = weight / height_meters**2
    print(f"Your BMI is {bmi:.1f}")

    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Healthy weight")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obesity range")