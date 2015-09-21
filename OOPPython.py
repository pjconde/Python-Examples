#Pablojose Conde 
#pjconde@gatech.edu

def isPalindrome(aString):
    if aString == "": ## Sets the base case, the base case being if the string is empty
        return True
    elif aString[0] == aString[-1]: ## Establishes a check to see if the first and last characters match
        aString = aString[1:-1] ## Cuts the string by cutting out the first character and last character
        return isPalindrome(aString) ## Recursive call
    else:
        return False

class BankAccount:

    def __init__(self, amount=0):
        self.balance = float(amount)
        self.numDeposits = 0
        self.numWithdraws = 0

    def getBalance(self):
        return(self.balance)

    def getWithdraws(self):
        return(self.numWithdraws)

    def getDeposits(self):
        return(self.numDeposits)

    def deposit(self, amount):
        self.balance += amount
        self.numDeposits += 1

    def withdraw(self, amount):
        if self.balance - amount > 0: ## Checks to make sure the withdraw amount does not make the account hit 0
            self.balance -= amount
            self.numWithdraws += 1
            return amount
        else:
            return -1 ## If amount withdrawn makes the account hit a negative it returns -1

    def batchDeposit(self, aFile):
        f = open(aFile)
        content = f.readlines()
        f.close()

        ## Function takes in a list of strings as a parameter. It takes the strings and trys to convert them to a
        ## float. If the string cannot be converted to a float it throws an exception returning False
        def isNum(aList):
                try:
                    float(aList)
                    return True
                except:
                    return False

        numList = filter(isNum, content) ## Filters using the getInt function
        amountList = map(float, numList) ## Makes a new list with the passed integers as floats
        numDeposits = len(amountList)    ## Gets the number of deposits made from the file
        total = reduce(lambda x,y: x+y, amountList)  ## Adds the list of floats to get a total

        self.balance += total ## Increases the balance in the account based on the numbers in the file
        self.numDeposits += numDeposits ## Increases the deposit count based on numbers in the file
