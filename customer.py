class Customer:
    fName = ""
    lName = ""
    accNum = 0
    balance = 0
    numOfCustomers = 0

    def __init__(self, fName, lName, accNum, balance):
        self.fName = fName
        self.lName = lName
        self.accNum = accNum
        self.balance = balance

    def getFName(self):
        return self.fName

    def getLName(self):
        return self.lName

    def getaccNum(self):
        return self.accNum

    def getbalance(self):
        return self.balance

    def setbalance(self, balance):
        self.balance = balance

    def setFName(self, fName):
        self.fName = fName

    def setLName(self, lName):
        self.lName = lName

    def setaccNum(self, accNum):
        self.accNum = accNum
