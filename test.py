import Wheel as Wheel
import controller as c
from xlrd import open_workbook
import re

# w = Wheel.Wheel('R01B-1711235', 'A207320', '17x8', '35', '5x112', '66.5', 'matt black', 'radius', '9')
# w.isEt('OE SPECS')

# wb = open_workbook('C:/Users/Cloudlin/Desktop/WheelSTK2.xlsx')
# sheet = wb.sheet_by_name('stock')
# number_of_rows = sheet.nrows
# number_of_columns = 9
# count = 0

# add wheels from spreadsheet
# wheels = []
# for row in range(1, number_of_rows):
#     values=[]
#     for col in range(number_of_columns):
#         value = (sheet.cell(row,col).value)
#         try:
#             if len(str(value)) <= 0:
#                 break
#         except ValueError:
#             pass
#         finally:
#             values.append(value)
#     if len(values) == 9:
#         count = count + 1
#         print(values)
#         wheel = Wheel.Wheel(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8])
#         wheels.append(wheel)


    # wheel = Wheel.Wheel(values[0], values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8])
    # wheels.append(wheel)

r1 = re.compile('[A-Z]-[0-9]+\.[0-9]/[A-Z]-[0-9]+\.[0-9]+')
r2 = re.compile('[0-9]+')

if r1.match('F-57.1/.56'): print('match')
if r2.match('60'): print('pewp')