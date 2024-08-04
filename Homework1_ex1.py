def convert_temp(temp, unit):
    if unit.upper() == 'C':
        return (temp - 32) * 5 / 9
    elif unit.upper() == 'F':
        return temp * 9 / 5 + 32

print(convert_temp(32, 'C'))
print(convert_temp(0,  'F'))
print(convert_temp(100,'C'))
print(convert_temp(100,'F'))
print(convert_temp(50, 'F'))
print(convert_temp(220,'C'))
