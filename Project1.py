# Comment like a fisherman not catching fish.

# Description: Honest Herry's User Car Lot program.
# Authour: Justin Seaward
# Date: July 11, 2025 - ??

# Define program laibraries.

import datetime
import FormatValues

# Define program constants.
CURR_DATE = datetime.datetime.now()

LICN_FEE_LOW = 75.00 # $75.00 on cars $15,000 and lower.

LICN_FEE_HIGH = 165.00 # $165.00 on cars $15,000 and higher.

HST_ESP = 0.15 # 15% for taxes.

LUX_TAX = 0.016 # 1.6% luxury tax after the sell price of $20,000.

FIN_FEE = 39.99 # $39.99 per year.


# Main program starts here.

while True:
    # Gather user information.
    
    while True:
        print()
        # Input and validations for customer first name.

        CustFN = "justin"#input("Enter the customers first name (END to quit): ").title()
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

    if CustFN.upper() == "END":
        break

        #print(CustFN) #test print.

    while True:
        # Input and validations for customer last name.

        print()
        CustLN = "seaward"#input("Enter the customers last name: ").title()
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
            print()
            PhoNum = "7092274569"#input("Enter the phone number (9999999999): ")
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

        print()
        PlateNum = "asd123"#input("Enter the plate number (LLL000): ").upper()
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
        # Input for car make.

        print()
        CarMake = "Honda"#input("Enter the car make (ie: Toyota): ")
        if CarMake == "":
            print()
            print("     Data Entry Error - Car make cannot be blank.")
            print()
        else:
            break

    while True:
        # Input for the Car Model.

        print()
        CarModel = "Civic"#input("Enter the car model (ie: Corolla): ")
        if CarModel == "":
            print()
            print("     Data Entry Error - Car model cannot be blank.")
            print()
        else:
            break

    while True:
         # Input for the Car Model.

        print()
        CarYear = "2013"#input("Enter the car year (ie: 1999): ")
        if CarYear == "":
            print()
            print("     Data Entry Error - Car year cannot be blank.")
            print()
        else:
            break

    while True:
        # Input and validation for sell price.

        print()
        SellPrice = 45000#input("Enter the Selling price: ")
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

        print()
        TradeAmt = 2500#input("Enter the trade in amount: ")
        TradeAmt = float(TradeAmt)
        if TradeAmt > SellPrice:
            print()
            print("     Date Entry Error - Trade-in amount of vehicle cannot exceed selling price.")
            print()
        else:
            break
        #print(TradeAmt) #test print. 

    while True:
        # Input and validation for sales persons name.

        print()
        SalesPersonName = "Mo"#input("Enter the sales person name: ")
        if SalesPersonName == "":
            print()
            print("    Data Entry Error - Customer name cannot be blank.")
            print()
        else:
            break
        #print(SalesPersonName) #test print

    # Start of program calculations.

    # Calculation for price after trade-in.
    PriAftTrade = SellPrice - TradeAmt

    # if statement for the licence fee.
    if SellPrice <= 15000:
        LincFee = LICN_FEE_LOW
    elif SellPrice > 15000:
        LincFee = LICN_FEE_HIGH
    else:
        break

    # Calculation for tranfer fee with if statement.
    TransFee = SellPrice * 0.01
    if SellPrice > 20000:
        TransFee = SellPrice * 0.016
    else:
        break    

    # Calculation for sub total.
    SubTotal = PriAftTrade + LincFee + TransFee

    # Calculation for taxes.
    TaxTotal = SubTotal * HST_ESP

    # Calculation for total sales price.
    TotalSales = SubTotal + TaxTotal

    # Recepit formats.

    # Format for sell price.
    SellPriceDsp = FormatValues.FDollar2(SellPrice)

    # Format for trade-in.
    TradeAmtDsp = FormatValues.FDollar2(TradeAmt)

    # Format for customer name.
    CustNameDsp = CustName = CustFN[0] + "." + " " + CustLN

    # Format for phone number.
    PhoNumDsp = "(" + PhoNum[0:3] + ")" + " " + PhoNum[3:6] + "-" + PhoNum[6:10] 

    # Format for car details.
    CarDetailsDsp = CarYear + " " + CarMake + " " + CarModel 

    # Format for price after trade-in.
    PriAftTradeDsp = FormatValues.FDollar2(PriAftTrade)

    # Format for license fee.
    LincDsp = FormatValues.FDollar2(LincFee)

    # Fromat for transfer fee:
    TransFeeDsp = FormatValues.FDollar2(TransFee)

    # Format for sub total.
    SubTotalDsp = FormatValues.FDollar2(SubTotal)

    # Format for HST.
    HSTDsp = FormatValues.FDollar2(TaxTotal)

    # Format for total sales.
    TotalSalesDsp = FormatValues.FDollar2(TotalSales)

    # Format for the Receipt ID.
    ReceiptID = CustFN[0] + CustLN[0] + "-" + PlateNum[3:6] + "-" + PhoNum[6:11]
    
    # Display receipt.
    print()
    print(f"         1.        2.        3         4         5.        6.        7.        8")
    print(f"12345678901234567890123456789012345678901234567890123456789012345678901234567890")
    print()
    # Invoice date format.
    CurrDateDsp = datetime.datetime.strftime(CURR_DATE, "%b %d, %Y")
    print(f"Honest Harry Car Sales                          Invoice Date:       {CurrDateDsp:>11s}     ")
    print(f"Used Car Sale And Receipt                       Receipt No:         {ReceiptID:>12s}       ")
    print()
    print(f"                                          Sale price:                 {SellPriceDsp:>10s}  ")
    print(f"Sold to:                                  Trade Allowance:            {TradeAmtDsp:>10s}   ")
    print(f"                                          --------------------------------------           ")
    print(f"     {CustNameDsp:<19s}                  Price after Trade:          {PriAftTradeDsp:>10s} ")
    print(f"      {PhoNumDsp:<14s}                      License Fee:                {LincDsp:>10s}     ")
    print(f"                                          Transfer Fee:               {TransFeeDsp:>10s}   ")
    print(f"                                          --------------------------------------           ")
    print(f"Car Details:                              Subtotal:                   {SubTotalDsp:>10s}   ")
    print(f"                                          HST:                        {HSTDsp:>10s}        ")
    print(f"     {CarDetailsDsp:<19s}                  --------------------------------------          ")
    print(f"                                          Total sales price:          {TotalSalesDsp:>10s} ")
    print(f"--------------------------------------------------------------------------------           ")
    print()
    print(f"                                  Financing        Total        Monthly                    ")
    print(f"      # Years       # Payments       Fee           Price        Payment                    ")
    print(f"      ----------------------------------------------------------------------               ")

    for Years in range(1, 5, 1):

        # Calculation for financing Fee:
        FinFee = FIN_FEE * Years

        # Calculation for total sales price
        TotalSalesPrice = TotalSales + FinFee

        # Calculation for Number of months:
        NumMons = Years * 12

        # Calculation for Monthly payment:
        MonPayment = TotalSalesPrice / NumMons

        # Format for payments.
        MonPaymentsDsp = FormatValues.FDollar2(MonPayment)

        # Format for financing fee.
        FinFeeDsp = FormatValues.FDollar2(FinFee)

        # Format for total sales price.
        TotalSalePriceDsp = FormatValues.FDollar2(TotalSalesPrice)

         # Adds an extra month to the number of months if the current day is >= 25th.
        if CURR_DATE.day >= 25:
            NumMons += 1

        print(f"          {Years}            {NumMons:<2d}       {FinFeeDsp:<7s}          {TotalSalePriceDsp:<10s}    {MonPaymentsDsp:<7s}")       
    print(f"      ----------------------------------------------------------------------               ")

    # First payment date:
    # Breaking up the current date into the day, month, year.
    CurrDay = CURR_DATE.day
    CurrMonth = CURR_DATE.month
    CurrYear = CURR_DATE.year

    CurrDatePlus1Month = datetime.datetime(CurrDay, CurrMonth + 1, CurrYear)
    FirPayDate = CurrDatePlus1Month

    FirPayDateDsp = datetime.datetime.strftime(FirPayDate, "%d-%b-%y")
    print(f"      First payment date: {FirPayDateDsp:<9s}")
    print(f"--------------------------------------------------------------------------------           ")

    Wait = input("Press enter key to continue.")

# Any housekeeping duties at the end of the program.