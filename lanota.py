import math
from decimal import *


getcontext().prec = 14
f = open("notedata.csv", "w", encoding='utf-8')
note = int(input())
# init values
base_note = Decimal(920000 / note)
combo_diff = Decimal(160000 / note)
# write point values
f.write("note count,," + str(note))
f.write("\nbase note score,," + str(base_note))
# tune = 10/23
f.write("\ntune note score,," + str(base_note * Decimal(10/23)))
f.write("\ncombo score unit,," + str(Decimal(combo_diff / note)) + "\n")
# half the combo unit is deducted from first note
first_note = Decimal(base_note + combo_diff - combo_diff / note / 2)
# write that down
f.write('"cumulative score data, might include ±1 due to rounding:"\n')
f.write("1," + str(first_note) + "," + str(first_note) + "," + str(int(first_note)) + "\n")
# from now to half the song size rounded down, one combo unit is deducted per note
half_size = math.ceil(note / 2)
if note % 2 == 0:
    half_size += 1
cumul = first_note
for i in range (2, half_size):
    first_note -= Decimal(combo_diff / note)
    cumul += Decimal(first_note)
    f.write(str(i) + "," + str(first_note) + "," + str(cumul) + "," + str(int(cumul)) + "\n")
# if note count is odd,
# the point value is quickly deducted over the next two notes
# so that the remainder is 25% of total combo score
# this is still affected by combo unit rules
# i.e. the first deduction is 0.75 units larger than the second
if note % 2 == 1:
    # get the decrement coefficient
    # equal to 1/4 chart size + 1
    cff = Decimal(note / Decimal(4.0) + 1)
    # get two deductions
    d1 = Decimal((cff + Decimal(0.75)) / 2)
    d2 = Decimal(cff - d1)
    # first deduction in place
    first_note -= Decimal(combo_diff / note * d1)
    cumul += Decimal(first_note)
    f.write(str(half_size) + "," + str(first_note) + "," + str(cumul) + "," + str(int(cumul)) + "\n")
    # same for the next
    first_note -= Decimal(combo_diff / note * d2)
    cumul += Decimal(first_note)
    f.write(str(half_size+1) + "," + str(first_note) + "," + str(cumul) + "," + str(int(cumul)) + "\n")
    # from now on till score is 1000000, note score no longer changes
    for i in range (half_size + 2, note + 1):
        cumul += Decimal(first_note)
        # larger chart size may cause 999999.9999999xx ~ 999999 like in dynamix
        if i != note:
            f.write(str(i) + "," + str(first_note) + "," + str(cumul) + "," + str(int(cumul)) + "\n")
        else:
            f.write(str(i) + "," + str(first_note) + "," + str(cumul) + ",1000000\n")
# if even, the difference is inflicted wholly at the next note
else:
    d = Decimal(note / Decimal(4.0)) + Decimal(0.5)
    # everything else is the same
    first_note -= Decimal(combo_diff / note * d)
    cumul += Decimal(first_note)
    f.write(str(half_size) + "," + str(first_note) + "," + str(cumul) + "," + str(int(cumul)) + "\n")
    for i in range (half_size + 1, note + 1):
        cumul += Decimal(first_note)
        if i != note:
            f.write(str(i) + "," + str(first_note) + "," + str(cumul) + "," + str(int(cumul)) + "\n")
        else:
            f.write(str(i) + "," + str(first_note) + "," + str(cumul) + ",1000000\n")
f.close()
