# I would choose value in directory because it can be excess via key & more easy to appoint the instance to run the transaction

# Sec2-Question 1

class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Account is created")

    def deposit(self):
        amount = float(input("Enter the amount to be deposit"))
        self.balance = self.balance + amount
        print("Deposit is sucessful and the balance in the account is %f" % self.balance)

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw"))
        if (self.balance >= amount):
            self.balance = self.balance - amount
            print("The withdraw is successful and balance is %d" % self.balance)
        else:
            print('Insufficient balance')

        def enquiry(self):
            print("Balance in the account is %f" % self.balance)


s = Bank_Account()
s.deposit()
s.withdraw()
s.deposit()


# Sec2-Question 2

def create_account():
    balance = 600

    def withdraw():  # asks for withdrawal amount, withdraws amount from balance, returns the balance amount
        counter = 0
        while counter <= 2:
            while counter == 0:
                withdraw = int(input("Enter the amount you want to withdraw: AED "))
                counter = counter + 1
            while ((int(balance) - int(withdraw)) < 0):
                print("Error Amount not available in card.")
                withdraw = int(input("Please enter the amount you want to withdraw again: AED "))
                continue
            while ((float(balance) - float(withdraw)) >= 0):
                tmp_balance -= withdraw
                print("Amount left in your account: AED " + str(tmp_balance))
                return tmp_balance
            counter = counter + 1

    def deposit():
        counter = 0
        while counter <= 2:
            while counter == 0:
                deposit = int(input("Enter amount to be deposited: "))
                counter = counter + 1
            while ((int(balance) + int(deposit)) >= 0):
                tmp_balance += deposit
                print("Amount left in your account: AED" + str(tmp_balance))
                return tmp_balance
            counter = counter + 1

    balance = withdraw()
    balance = deposit()