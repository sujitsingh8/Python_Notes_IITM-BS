''' User Defined Exceptions- '''

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise Exception("You are underage, can not vote!")

    print("You are eligible to vote")

except ValueError:
    print("Invalid input! Please enter numbers only.")

except Exception as e:
    print(e)