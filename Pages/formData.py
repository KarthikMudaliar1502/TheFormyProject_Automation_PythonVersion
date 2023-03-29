import xlrd

workbook = xlrd.open_workbook("data.xlsx")
sheet = workbook.sheet_by_name("Sheet1")

# get total number of rows and columns

rowCount = sheet.nrows
colCount = sheet.ncols

for curr_row in range(1, rowCount):
    first_name = sheet.cell_value(curr_row, 0)
    last_name = sheet.cell_value(curr_row, 1)
    job_title = sheet.cell_value(curr_row, 2)
    education = sheet.cell_value(curr_row, 3)
    gender = sheet.cell_value(curr_row, 4)
    experience = sheet.cell_value(curr_row, 5)
    date = sheet.cell_value(curr_row, 6)