print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
num_of_people = int(input("How many people to split the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
bill_with_tip = total_bill * (1 + tip_percentage / 100)
bill_per_person = bill_with_tip / num_of_people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")