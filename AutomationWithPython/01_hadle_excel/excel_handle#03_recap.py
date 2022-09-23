import openpyxl as excel

book = excel.Workbook()
sheel = book.active
sheel["A1"] = "Name"
sheel["A2"] = "Age"
sheel["A3"] = "E-mail"

sheel["B1"] = "tylone"
sheel["B2"] = "42"
sheel["B3"] = "didmaehd@gmail.com"

book.save("./output/list.xlsx")


book = excel.load_workbook("./output/list.xlsx")
sheet1 = book.worksheets[0]
cell = sheet1["B3"]
print(cell.value)