print("Welcome to the tip calculator")
#float
total_bill = float(input("What was the total bill? $"))
#percent
tip = int(input("How much tip would you like to give? 10,12, or 15?"))
#int
people_split = int(input("How many people to split the bill?"))

#ans should be rounded to 2 decimal places
bill_per_person= (total_bill + (total_bill*(tip/100)))/people_split
final_amount = round(bill_per_person,2)

print(f"Each person should pay ${final_amount}")