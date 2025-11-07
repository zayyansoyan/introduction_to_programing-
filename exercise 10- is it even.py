def is_even_or_odd(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def main():
    num = int(input("Enter a number: "))
    result = is_even_or_odd(num)
    print(result)

if __name__ == "__main__":
    main()
