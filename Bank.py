from customer import Customer

bName = input("Enter the bank section 1,2 or 3: ")
cusNo = int(input("Enter The Number of customers: "))
choice = 0


class Bank:
    bName = " "
    customers = [None] * cusNo

    def createAccount(self):
        accNum = int(input("Enter the account number: "))
        fName = input("Enter The customer first Name:")
        lName = input("Enter The customer last Name : ")
        balance = int(input("Enter the initial amount: "))
        c = Customer(fName, lName, accNum, balance)
        Customer.numOfCustomers = c
        print("The amount in:", c.getaccNum(), " for ", c.getFName(), " is ", c.getbalance())

    def searchAccount(self, customers):
        num = int(input("Enter the number of the of the account record you want to display : "))
        flag = 0
        for n in range(Customer.numOfCustomers):
            if customers[n].getaccNum() == num:
                print("Account record for ", customers[n].getFName(), " ", customers[n].getLName(), " AccountNumber # ",
                      customers[n].getaccNum())
                print("The balance in her/his account is: ", customers[n].getbalance())
            flag = 1
            if flag == 0:
                print("ERROR:there is no account for this customer")

    def displayAllAccounts(self, customers):
        if Customer.numOfCustomers == 0:
            print("there is no account ")
        else:
            for j in range(Customer.numOfCustomers):
                print("Customer name is ", customers[j].getFName(), " ", customers[j].getLName())
                print("Account number is ", customers[j].getaccNum())
                print(" Customer balance:", customers[j].getbalance())

    def deposit(self, customers):
        num = int(input("Enter the number of the of the account record you want to deposit in : "))
        flag = 0

        for n in range(Customer.numOfCustomers):
            if customers[n].getaccNum() == num:
                deposit_amount = int(input("Enter the deposit amount: "))
                d = customers[n].getbalance()
                d += deposit_amount
                customers[n].setbalance(d)
                print("The deposit process is done successfully")
            flag = 1
            if flag == 0:
                print("ERROR:there is no account for this customer")

    def withdraw(self, customers):
        global w, withdraw_amount
        num = int(input("Enter the number of the of the account record you want to withdraw fro3"
                        "m : "))
        flag = 0
        for n in range(Customer.numOfCustomers):
            if customers[n].getaccNum() == num:
                withdraw_amount = int(input("Enter the withdraw amount: "))
            if customers[n].getbalance() >= withdraw_amount:
                w = customers[n].getbalance()
                w -= withdraw_amount
            customers[n].setbalance(w)
            print("The withdraw process is done successfully")
        flag = 1

        if flag == 0:
            print("ERROR:there is no account for this customer")
