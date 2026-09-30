# TG, Functions notes

def stupid_proof(money):
    while True:
      try:
           amount = float(input(f"What is your monthly{money}:"))
           return amount
      except:
            print("That isn't a number :( )")


# Write all your variable 
income = stupid_proof("income")

rent = stupid_proof("rent")

utilities = stupid_proof("utilities")

groceries = stupid_proof("groceries")

transportation = stupid_proof("transportation")

saveings = income * .1

# Write any functions you are useing
def calc_percent(income, bill):
    return round(bill/income *100) 
 
# Outputs for the user
print(f"Your rent is ${rent:.2f} that is {calc_percent(income,rent)}% of your income.")

print(f"Your utilities is ${utilities:.2f} that is {calc_percent(income,rent)}% of your income.")

print(f"Your groceries is ${groceries:.2f} that is {calc_percent(income,rent)}% of your income.")

print(f"Your transportation is ${transportation:.2f} that is {calc_percent(income,rent)}% of your income.")

print(f"Your saveings is ${saveings:.2f} that is {calc_percent(income,rent)}% of your income.")

