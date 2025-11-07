def main():
    f = "python"
    password = ""

    while password != f:
        password = input("Enter the password: ")
        if password == f:
            print("Access granted.")
        else:
            print("Incorrect password. Try again.")

if __name__ == "__main__":
    main()
