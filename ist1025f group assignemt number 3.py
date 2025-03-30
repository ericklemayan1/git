def main():
    # List of days of the week
    day_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Initialize an empty list to store temperatures
    temperatures = []

    # Get the temperature for each day of the week
    for day in day_of_week:
        temp = float(input(f"Enter the temperature for {day}: "))  
        temperatures.append(temp) # Store the temperature in the list

    # Calculate
    lowest_temperature = min(temperatures)
    highest_temperature = max(temperatures)
    total_temperature = sum(temperatures)
    avg_temperature = total_temperature / 7 
    print()

   
    print(f"Lowest Temperature: {lowest_temperature:.2f}")
    print(f"Highest Temperature: {highest_temperature:.2f}")
    print(f"Total Temperature: {total_temperature:.2f}")
    print(f"Average Temperature: {avg_temperature:.2f}")

main()
