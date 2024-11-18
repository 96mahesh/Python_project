import openpyxl

wb = openpyxl.load_workbook("C:\\Users\\Admin\\TrueBoardWorkplace\\Truboard\\truboard.1\\truboard\\src\\main\\resources\\Test_Data\\TestData_TG\\TestData_TruGenie.xlsx")
print(wb.sheetnames)
ws = wb['Final Noc']
print(ws)

ws1 = wb['PMC']
print(ws1)
