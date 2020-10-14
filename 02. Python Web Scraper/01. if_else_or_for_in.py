def age_check(age):
    print(f"you are {age}")
    if age < 18:
        print("you cannot drink")
    elif age == 18:
        print("congrats!")
    else:
        print("enjoy youre drink")

age_check(18)

print()

days = ("Mon", "Tue", "Wed", "Thur", "Fri")

for day in days:
    if day is "Wed":
        break
    else:
        print(day)
