_1stSemester = int(input('Enter 1st semester grade'))
_2ndSemester = int(input('Enter 2nd semester grade'))
_3rdSemester = int(input('Enter 3rd semester grade'))
_minGradePointAverage = 21

_gradePointAverage = _1stSemester + _2ndSemester + _3rdSemester

if (_gradePointAverage >= _minGradePointAverage):
       print ("Congratulations, you're approved")
else:
       print ("We are sad to inform that you're not approved")
          
