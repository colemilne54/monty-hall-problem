import random
import xlwt
from xlwt import Workbook

list = ["car", "zonk1", "zonk2"]

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

for x in range (100):
    randlist = random.sample(list, 3)

    pick = random.randint(1,3)
    firstpick = int(pick)
    firstpickindex = firstpick - 1

    if randlist[firstpickindex] != "zonk1":
        shown = 'zonk1'
    else:
        shown = 'zonk2'

    if shown == 'zonk1':
        finalpick = [x for x in list if x not in [randlist[randlist.index('zonk1')], randlist[firstpickindex]]]
        finalpickitem = finalpick[0]
        finalpickindex = randlist.index(finalpickitem)
    elif shown == 'zonk2':
        finalpick = [x for x in list if x not in [randlist[randlist.index('zonk2')], randlist[firstpickindex]]]
        finalpickitem = finalpick[0]
        finalpickindex = randlist.index(finalpickitem)

    if randlist[finalpickindex] != 'car':
        sheet1.write(x, 0, '0')
    elif randlist[finalpickindex] == 'car':
        sheet1.write(x, 0, '1')

wb.save('store.xlsx')



