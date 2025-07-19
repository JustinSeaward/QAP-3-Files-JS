# Library of functions for formatting numbers and dates.

import datetime

# Define program constants.

LICN_FEE_LOW = 75.00 # $75.00 on cars $15,000 and lower.

LICN_FEE_HIGH = 165.00 # $165.00 on cars $15,000 and higher.

HST_ESP = 0.15 # 15% for taxes.

LUX_TAX = 0.016 # 1.6% luxury tax after the sell price of $20,000.

FIN_FEE = 39.99 # $39.99 per year.

def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.

    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr


def FComma2(Value):
    # Function will accept a value and format it to #,###.##.

    ValueStr = "{:,.2f}".format(Value)

    return ValueStr


def FComma0(Value):
    # Function will accept a value and format it to #,###.

    ValueStr = "{:,.0f}".format(Value)

    return ValueStr


def FNumber0(Value):
    # Function will accept a value and format it to ####.

    ValueStr = "{:.0f}".format(Value)

    return ValueStr


def FNumber1(Value):
    # Function will accept a value and format it to ####.#.

    ValueStr = "{:.1f}".format(Value)

    return ValueStr


def FNumber2(Value):
    # Function will accept a value and format it to ####.##.

    ValueStr = "{:.2f}".format(Value)

    return ValueStr


def FDateS(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr


def FDateM(DateValue):
    # Function will accept a value and format it to dd-Mon-yy.

    DateValueStr = DateValue.strftime("%d-%b-%y")

    return DateValueStr


def FDateL(DateValue):
    # Function will accept a value and format it to Day, Month dd, yyyy.

    DateValueStr = DateValue.strftime("%A, %B %d, %Y")

    return DateValueStr


### New Functions ###

# Function to determine Licening fee.
def LicenceFee(SellPrice):

    if SellPrice <= 15000:
        LincFee = LICN_FEE_LOW
    elif SellPrice > 15000:
        LincFee = LICN_FEE_HIGH

    return LincFee

# Function to determine the Transfer Fee
def TransferFee(SellPrice):

    TransFee = SellPrice * 0.01
    if SellPrice > 20000:
        TransFee = SellPrice * 0.016

    return TransFee


def FirstPayDate(CurrentDate):

    CurrentDate = datetime.datetime.now()

    Year = CurrentDate.year
    Month = CurrentDate.month
    Day = CurrentDate.day

    PayYear = Year
    PayMonth = Month + 1
    PayDay = 1

    if Day > 25:
        PayMonth += 1
    
    if PayMonth > 12:
        PayMonth -= 12
        PayYear += 1

    PayDate = datetime.datetime(PayYear, PayMonth, PayDay)
    PayDateDsp = datetime.datetime.strftime(PayDate, '%d-%b-%y')

    return PayDateDsp


