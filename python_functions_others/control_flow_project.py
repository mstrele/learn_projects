#function that analyzes an individual’s smoking status
def analyze_smoker(smoker_status):
    if smoker_status == 1:
        print("To lower your cost, you should consider quitting smoking.")
    else:
        print("Smoking is not an issue for you.")

#function that analyzes an individual’s BMI
def analyze_bmi(bmi_value):
    if bmi_value > 30:
        # notify the individual how much they need
        # to lower their BMI to bring it to a normal weight range
        
        print("Your BMI is in the obese range. To lower your cost, you should lose " + str(bmi_value - 24) + " kg.")
    elif bmi_value >= 25 and bmi_value <= 30:
        print(
            "Your BMI is in the overweight range. To lower your cost, you should lose " + str(bmi_value - 24) + " kg.")
    elif bmi_value >= 18.5 and bmi_value < 25:
        print("Your BMI is in a healthy range.")
    else:
        print(
            "Your BMI is in the underweight range. To become healthy, you should gain " + str(24 - bmi_value) + " kg.")


# function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
    print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
    analyze_smoker(smoker)
    analyze_bmi(bmi)
    return estimated_cost


try:
    me_insurance_cost = estimate_insurance_cost(name='Dieas', age=23, sex=1, bmi=16, num_of_children=1, smoker=1)
except:
    print("Hmmmm")