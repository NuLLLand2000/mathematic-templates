from excel_operations import read_and_write as rw
from function_operation import poly_fit as pf


my_file = rw.read_file("test_file.xlsx")
my_sheet = rw.read_sheet(my_file, 0)
line1 = rw.read_row(my_sheet, 0, 0, 10)

print(line1)

print("asasasasas")
