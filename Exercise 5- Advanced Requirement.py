def main():
    month = int(input("Enter the month number: "))
    if month == 2:
        leap = input("Is it a leap year? (yes/no): ").lower()
        if leap == "yes":
            days = 29
        else:
            days = 28
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        days = 31
    elif month in [4, 6, 9, 11]:
        days = 30
    else:
        print("Invalid month number!")
        return

    print(f"The month you entered has {days} days.")

if __name__ == "__main__":
    main()
