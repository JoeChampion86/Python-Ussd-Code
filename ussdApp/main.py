#Fund Transfer
def fundTransfer():
    acct = input("Enter Account Number: ")
    if acct.isnumeric():
        print(f"This {acct}  has been debited 50,000 naira")
    else:
        print(
            "Invalid Transfer\n"
            "Try Again"
        )
        fundTransfer()
#Enter Amount
def checkAmount(x):
    amount = input("Enter Amount: ")
    if amount.isnumeric():
        print(f"The {x} has been credited with {amount}")
    else:
        print(
            "Invalid Amount Entry\n"
            "Try Again"
        )
        checkAmount(x)
#Airtime Transaction
def airtimeTrans():
    phone = input("Enter Phone Number: ")
    if len(phone) == 11 and phone.isnumeric():
        checkAmount(phone)
    else:
        print(
            "Invalid Phone Number\n"
            "Try Again"
        )
        airtimeTrans()

#Transaction Entry
def transEntry():
    transCode = input(
        "1. Check Balance\n"
        "2. Buy Airtime\n"
        "3. Fund Transfer\n"
        "Select Transaction: "
    )
    if transCode == "1":
        print("Your Account Balance is 200,000 naira")
    elif transCode == "2":
        airtimeTrans()
    elif transCode == "3":
        fundTransfer()
    else:
        print(
            "Invalid Transaction\n"
            "Try Again"
        )
        transEntry()
#Function to cross-check ussd code
def confirmussd():
    ussd = input("Enter Ussd Code: ")
    if ussd == "*123#":
        transEntry()
    else:
        print("Invalid Ussd Code\n"
          "Try Again"
        )
        confirmussd()

#Calling the Function
confirmussd()
