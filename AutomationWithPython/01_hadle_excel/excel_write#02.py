# for 문을 이용해서 연속으로 값 넣기

import openpyxl as excel
book = excel.Workbook()
sheet = book.active

for i in range(10):
    sheet.cell(row=(i+1), column=1, value=(i+1))

book.save("./output/write_column.xlsx")
