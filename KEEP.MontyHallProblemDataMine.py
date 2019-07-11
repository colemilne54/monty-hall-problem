import random
import xlwt
from xlwt import Workbook

list = ["car", "zonk1", "zonk2"]

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

for x in range(100):
    randlist = random.sample(list, 3)
    pick = random.randint(1,3)
    firstpick = int(pick)
    firstpickindex = firstpick - 1

    finalpickindex = firstpickindex

    if randlist[finalpickindex] != 'car':
        sheet1.write(x, 0, '0')
    elif randlist[finalpickindex] == 'car':
        sheet1.write(x, 0, '1')

wb.save('store.xlsx')