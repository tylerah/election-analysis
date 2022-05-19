# What is the score?
score = float(input("What is your first test score?"))

# Determine grade
if score >= 90:
    print('Your grade is an A')
else:
    if score >= 80:
        print('Your grade is a B')
    else:
        if score >= 70:
            print('Your grade is a C')
        else:
            if score >= 60:
                print('Your grade is a D')
            else:
                print('Your grade is an F')

score_2 = float(input("What is your second test score?"))

# Determine second grade

if score_2 >= 90:
    print('A')
elif score_2 >= 80:
    print('B')
elif score_2 >= 70:
    print('C')
elif score_2 >= 60:
    print('D')
else:
    print('F')


