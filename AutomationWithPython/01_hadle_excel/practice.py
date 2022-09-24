import openpyxl as excel

book = excel.Workbook()
sheet = book.active
cell = sheet.cell(row=1,column=1)
cell.value = "abc"

print(cell.value)

cell2 = sheet.cell(row=1,column=2,value="def")

print (cell2.value)

cell3 = sheet.cell(row=1,column=3)
cell3.value = cell3.coordinate
print(cell3.value)
