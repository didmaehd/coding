import openpyxl as excel # import openpyxl and rename to excel
book = excel.Workbook() # create workbook
sheet = book.active # create sheet
sheet["A1"] = "How are you?" # insert text to A1 on excel 
book.save("./output/hello.xlsx") # save file


sheet["A2"] = "I'm fine, thank you!"
book.save("./output/hello.xlsx")


sheet["A3"] = "Get out of here!"
book.save("./output/hello.xlsx")

sheet["B1"] = "ABC"
book.save("./output/hello.xlsx")
