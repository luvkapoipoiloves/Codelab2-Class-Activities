year = 2
Class = "CY"
if year == "1":
    if Class.upper() == "A":
        print("You belong to class - CY and Year 1")
    else:
        print(f"You belong to class - {Class} and Year 1")
elif year == "2":
    if Class.upper() == "B":
        print("You belong to class - CY and Year 2")
    else:
        print(f"You belong to class - {Class} and Year 2")
else:
    print(f"You belong to class - {Class} and Year {year}")
