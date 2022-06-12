# -- Tip Calculator --
# 100 days code of Python
# Pandu Purwadi

# Greeting and information for user
print("Welcome! This is Tip Calculator")

#User Input Information
total_bill = float(input("What was the total bill? $"))
percent_tip = int(input("What percentage tip would you like to give?"))
person_count = int(input("How many people to split the bill?"))

#Calculation
percent_convert = percent_tip/100
each_person_pay = round((total_bill + (total_bill*percent_convert)) / person_count, 2)

#Result
print(f"Each person should pay: ${each_person_pay}")