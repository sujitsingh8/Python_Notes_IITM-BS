''' User Defined Exceptions- '''

balance = 5000
withdraw = int(input("Enter amount to withdraw: "))

if withdraw > balance:
    raise Exception("Insufficient balance")

balance = balance - withdraw
print("Transaction successful")
print('Remaining Balance:',balance)