def calculate_bmi(weight, height):
    
    bmi = weight / (height ** height)
    return bmi

def categorize_bmi(bmi):
   
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Please enter positive numbers for both weight and height.")
            return

        
        bmi = calculate_bmi(weight, height)

        
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {categorize_bmi(bmi)}")
        
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")


if __name__ == "__main__":
    main()

print("1.Inganji fiscal clovis,2.Isingizwe luckyson,3.Kirabo lucille,4,Gasore boris")

