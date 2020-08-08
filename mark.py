mark = float (input('please enter your exam  grade ? '))
if 0 <= mark < 50 :
    print('yor grade is F ')
elif 50 <= mark < 65 :
    print('yor grade is D ')
elif 65 <= mark < 75 :
    print('yor grade is C ')
elif 75 <= mark < 85 :
    print('yor grade is B ')
elif 85 <= mark <= 100 :
    print('yor grade is A ')
else :
    print("your grade must be between 0 and 100 unless you haven't went to the exam" )