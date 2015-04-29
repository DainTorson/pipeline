import pro_unit

divident = [1, 1, 0, 1]
divider = [0, 1, 1, 0]
#regP = [0, 0, 0, 0, 0]

print(divident)
print(divider)
#print(regP)

divident.reverse()
divider.reverse()
#regP.reverse()

unit = pro_unit.ProUnit()
unit.start(divident, divider)

for dummy_idx in range(len(divident)):
	print(unit)
	unit.perform_step()

divident = unit.get_regA()
divider = unit.get_regB()
regP = unit.get_regP()

divident.reverse()
divider.reverse()
regP.reverse()

print()
print(divident)
print(divider)
print(regP)

