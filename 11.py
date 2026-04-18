''' User Defined Exceptions- '''

try:
    balance = 5000
    withdraw = int(input("Enter amount to withdraw: "))

    if withdraw > balance:
        raise Exception("Insufficient balance")

    balance = balance - withdraw
    print("Transaction successful")
    print("Remaining Balance:", balance)

except ValueError:
    print("Invalid input! Please enter valid Amount.")

except Exception as e:
    print(e)