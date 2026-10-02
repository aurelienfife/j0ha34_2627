# This will test if you can enter the nightclub

def check_age(age):
    if age >= 18:
        return True
    else:
        return False

def double_check():
    print("I don't believe you.")
    another = int(input("Say your age again"))
    res = check_age(another)
    if res is True:
        print("Okay okay...")
    else:
        print("See? you lied")


agecheck = int(input("ID check: how old are you?"))
result = check_age(agecheck)

if result is True:
    double_check()
else:
    print("You cannot come in")

