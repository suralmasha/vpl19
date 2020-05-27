import openpyxl
import xlrd
import csv
import xlwt
excel = xlrd.open_workbook('my_func_data.xlsx')
sheet = excel.sheet_by_index(0)
uwu = []
owo = []
row = 0
book=xlrd.open_workbook('my_func_data.xlsx')

def excel_help_1():
    global row    
    global kekw
    global uwu
    global cell
    col =- 1
    kekw = []
    if col < 6:
        col += 1
    if col == 0 or col == 1 or col == 3 or col == 5:
        cell = sheet.cell(row,col)
        kekw.append(cell.value)
        owo.append(kekw)

def excel_help_2():
    global meow
    global owo
    global row
    global cell
    meow = []
    col = -1
    while col < 6:
        col += 1
        if col == 0 or col == 2 or col == 4 or col == 6:
            cell = sheet.cell(row,col)
            meow.append(cell.value)
            owo.append(meow)
while row < sheet.nrows:
       excel_help_1()
       excel_help_2()
       row += 1

file1 = open('accuracy.csv', 'w')
with file1:
    finally_write = csv.writer(file1, delimiter = '-')
    finally_write.writerows(uwu)

file2 = open('performance.csv', 'w')
with file2:
    finally_write = csv.writer(file2, delimiter = '-')
    finally_write.writerows(owo)
