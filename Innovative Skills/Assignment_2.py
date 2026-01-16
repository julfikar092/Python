while True:
    day_of_the_week_input = input("Enter any day of a week (e.g., Monday): ")

    day_of_the_week = day_of_the_week_input.lower()

    valid_days = ["saturday","sunday","monday","tuesday","wednesday","thursday","friday"]

    if day_of_the_week in valid_days:
        break

    else:
        print(f"Error: '{day_of_the_week_input}' is not a valid day. Please try again")


while True:
    time_of_visit_input = input("Enter time for visiting restaurant (24 hour format, e.g., 17.5 for 5:30 PM): ")
    try:
        time_of_visit = float(time_of_visit_input)

        if 0.0 <= time_of_visit <= 24.00:
            break

        else:
            print("Error: Time must be between 0.0 and 24.0. Please try again.")

    except ValueError:
         print(f"Error: '{time_of_visit_input}' is not a valid number. Please use a format like 14.0 or 18.5.")

print(f"\nCalculating discount for {day_of_the_week.capitalize()} at {time_of_visit} hour")


if day_of_the_week in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    if time_of_visit < 17.0: 
        print("No discount")
    else: 
        print("10% discount on the total bill amount")


elif day_of_the_week in ["saturday", "sunday"]:
    if time_of_visit < 15.0: 
        print("5% discount on the total bill amount")
    else: 
        print("7% discount on the total bill amount")