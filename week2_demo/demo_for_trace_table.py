# Trace table example

name = input("What is your name?")

qty = int(input("How many red bulls do you want?"))
yesterday = int(input("How many have you had yesterday?"))
qty = qty - yesterday
print(f"{name}, you can only buy {qty}")

unit_price = 2.60
total = qty*unit_price

print(f"That's £{total}")
