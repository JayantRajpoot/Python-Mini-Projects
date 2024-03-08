#tip calculator with if and else statement.
print ("Welcome to the tip calculator.")
bill= (input("what is the total bill? ₹"))
bill1= int(bill)
age= int(input("What's your age?"))
if (age >= 15):
    tip= (input("what percentage of the bill you want to tip? 5 8 or 10? "))
    tip1= int(tip)
    tip_calculate= (bill1 * tip1 /100)
    people= (input("How many people are splitting the bill? "))
    people1= int(people)
    people_splitting= (bill1 + tip_calculate) / people1
    print (f"Each person should pay₹ {people_splitting}")
else:
    people= (input("How many people are splitting the bill? "))
    people1= int(people)
    people_splitting= (bill1) / people1
    print (f"Each person should pay₹ {people_splitting}")