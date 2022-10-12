#셀 수소를 입력

import openpyxl as excel

book = excel.Workbook()
sheet = book.active

for a in range (1,31):
    for b in range (1,31):
        cell = sheet.cell(row=a,column=b)
        cell.value = cell.coordinate

book.save("./output/write_cellname.xlsx")