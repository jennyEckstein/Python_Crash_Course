
# if else elif == != > >= <=

age = 21

if age > 16 :
    print 'You are old enough to drive'
else:
    print 'You are not old enough to drive'

if age >= 21:
    print 'Drink'
elif age >= 16: # else if
    print 'Not Legal to drink'
else:
    print 'Definately no alcohol'


# logical operators and or not

if (age >= 1) and (age <= 18):
    print 'You are between 1 and 18 years old'
elif (age == 21) or (age >= 65):
    print 'You are between 21 and 65'
elif not(age == 30):
    print 'You are thirty'
else:
    print 'Some other age'