# Darrell Lawson
# CIS 261 
# Course Project Phase 2

from datetime import datetime


def GetEmpName():
    return input("Enter employee name (END to terminate): ")

def GetDatesWorked():
    while True:
        fromdate = input("Enter Start Date(mm/dd/yyyy): ")
        todate = input("Enter End Date(mm/dd/yyyy): ")
        try:
            fromdate = datetime.strptime(fromdate, "%m/%d/%Y")
            todate = datetime.strptime(todate, "%m/%d/%Y")
            return fromdate, todate
        except ValueError:
            print("The format was not correct, try again please.")


def GetHoursWorked():
    return float(input('Enter amount of hours worked:  '))

def GetHourlyRate():
    return float(input("Enter hourly rate: "))

def GetTaxRate():
    return float(input("Enter tax rate: "))

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    for EmpList in EmpDetailList:
        fromdate, todate, empname, hours, hourlyrate, taxrate = EmpList

def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00

    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]

        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)

        print("Name: ", empname)
        print("FromDate: ", fromdate)
        print("To Date: ", todate)
        print("Hours Worked: ", f"{hours:,.2f}")
        print("Hourly Rate: ", f"{hourlyrate:,.2f}")
        print("Gross Pay: ", f"{grosspay:,.2f}")
        print("Tax Rate: ", f"{taxrate:,.1%}")
        print("Income Tax: ", f"{incometax:,.2f}")
        print("Net Pay: ", f"{netpay:,.2f}")
        print()

        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay

    print("Total Employees: ", TotEmployees)
    print("Total Hours: ", f"{TotHours:,.2f}")
    print("Total Gross Pay: ", f"{TotGrossPay:,.2f}")
    print("Total Income Tax: ", f"{TotTax:,.2f}")
    print("Total Net Pay: ", f"{TotNetPay:,.2f}")

    EmpTotals["TotEmp"] = TotEmployees
    EmpTotals["TotHours"] = TotHours
    EmpTotals["TotGrossPay"] = TotGrossPay
    EmpTotals["TotTax"] = TotTax
    EmpTotals["TotNetPay"] = TotNetPay

def PrintTotals(EmpTotals):    
    print()
    print(f'Total Number Of Employees: {EmpTotals["TotEmp"]}')
    print(f'Total Hours Worked: {EmpTotals["TotHours"]:.2f}')
    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]:,.2f}')
    print(f'Total Income Tax: {EmpTotals["TotTax"]:,.2f}')
    print(f'Total Net Pay: {EmpTotals["TotNetPay"]:,.2f}')
    
if __name__ == "__main__":

    EmpDetailList = []
    EmpTotals = {}
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()
        
        EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]
        EmpDetailList.append(EmpDetail)
        
    printinfo(EmpDetailList)
    PrintTotals (EmpTotals)
