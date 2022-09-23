#기존 파일 불러오기

#openpyxl을 import하고 excle로 이름 바꾸기
import openpyxl as excel

#hello.xlsx 파일을 불러와서 book변수에 담기
book = excel.load_workbook("./output/hello.xlsx") 

#workbook의 첫번째 워크시트 가져와서 sheet변수에 담기
sheet = book.worksheets[0]

#시트에서 cell A1 가져와서 cell 변수에 담기
cell = sheet["A1"]

print(cell)
print(cell.value)
