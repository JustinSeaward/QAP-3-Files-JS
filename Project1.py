# Comment like a fisherman not catching fish.

# Description: Honest Herry's User Car Lot program.
# Authour: Justin Seaward
# Date: July 11, 2025 - ??

# Define program laibraries.
import datetime

# Define program constants.
CURR_DATE = datetime.datetime.now

LICN_FEE_LOW = 75.00 # $75.00 on cars $15,000 and lower.

LICN_FEE_HIGH = 165.00 # $165.00 on cars $15,000 and higher.

HST_ESP = 0.15 # 15% for taxes.

LUX_TAX = 0.016 # 1.6% luxury tax after the sell price of $20,000.

FIN_FEE = 39.99 # $39.99 per year.


# Main program starts here.

while True:
    # Gather user information.
    # Input and validations for customer first name.

    while True:
        print()
        CustFN = input("Enter the customers first name (END to QUIT): ").title()
        if CustFN == "":
            print()
            print("   Data Entry Error - Customer first name cannot be blank.")
            print()
        elif CustFN.isalpha() == False:
            print()
            print("     Data Entry Error - Invalid characters, must contain letters only.")
            print()
        else:
            break

        #print(CustFN) #test print.

    while True:
        # Input and validations for customer last name.
        CustLN = input("Enter the customers last name (END to QUIT): ").title()
        if CustLN == "":
            print()
            print("    Data Entry Error - Customer last name cannot be blank.")
            print()
        elif CustLN.isalpha() == False:
            print()
            print("    Data Entry Error - Invalid characters, must contain letters only.")
            print()
        else:
            break

        #print(CustLN) #test print.

    while True:
        # Input and validations for phone number.
        try:
            PhoNum = input("Enter the phone number (7091235678): ")
            if PhoNum == "":
                print()
                print("    Data Entry Error - Phone number canot be blank.")
                print()
                continue
        except ValueError:
            print()
            print("    Data Entry Error - Phone number contains invalid characters.")
            print()
        else:
            if len(PhoNum) != 10:
                print()
                print("    Data Entry Error - Phone number has to contain 10 characters.")
                print()
            else:
                break

        #print(PhoNum) #test print.

    while True:
        # Input and validations for plate number.
        PlateNum = input("Enter the plate number (LLL000): ").upper()

        if PlateNum == "":
            print()
            print("    Date entry error - Plate number cannot be blank.")
            print()
        elif len(PlateNum) < 6 and len(PlateNum) > 6: 
            print()
            print("   Data Entry Error - Plate number must be 6 characters.")
            print()
        elif  PlateNum[0:3].isalpha() == False:
            print()
            print("    Date entry error - first 3 characters of the plate number must be letters (A - Z).")
            print()
        elif  PlateNum[3:6].isdigit() == False:
            print()
            print("    Date entry error - last 3 characters of the plate number must be numbers (0-9).")
            print()
        else:
            break
        #print(PlateNum) #test print.

    while True:
        # Input and validation for sell price.
        SellPrice = input("Enter the Selling price: ")
        SellPrice = float(SellPrice)
        if  SellPrice > 50000:
            print()
            print("      Date Entry Error - Selling price of vehicle cannot exceed 50,000.")
            print()
        else:
            break
        print(SellPrice) #test print.

    while True:
        # Input and validations for trade-in amount.
        TradeAmt = input("Enter the trade in amount: ")
        TradeAmt = float(TradeAmt)
        if TradeAmt > SellPrice:
            print()
            print("     Date Entry Error - Trade in amount of vehicle cannot exceed Selling Price.")
            print()
        else:
            break
        #print(TradeAmt) #test print. 

    while True:
        SalesPersonName = input("Enter the sales person name: ")
        if SalesPersonName == "":
            print()
            print("    Data Entry Error - Customer name cannot be blank.")
            print()
        elif SalesPersonName.isalpha() == False:
            print()
            print("    Data Entry Error - Invalid format, must contain letters only.")
            print()
        else:
            break
        #print(SalesPersonName) #test print

    

# Any housekeeping duties at the end of the program.