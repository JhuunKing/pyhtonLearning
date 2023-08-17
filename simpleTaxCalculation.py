_Wage = float(input('Enter the value'))
_minimumWage = 1200
_incomeTax = _Wage > _minimumWage

if (_incomeTax):
    print ('Tax is required')
else:
    print ('Tax is not required')