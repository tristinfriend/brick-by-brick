'''
COS 121
Homework #4
By Tristin Friend
Professor Troy Shotter
10/21/2024
'''

#Help from in lab

userinput = int(input('Enter a number'))
#Task 1 ^

#Standard Triangle
for row in range(userinput): #Every single shape should start with this line
    for col in range(row+1):
        print('x', end='')
    print()
print('-----')


#Upside Down Triange
for row in range(userinput):
    for col in range(userinput-row):
        print('x', end='')
    print()
print('-----')


#The Ramp
for row in range(userinput):
    for col in range(userinput-(row+1)): 
        print(' ', end='')
    for col in range(row +1):
        print('x', end='')
    print()
print('-----')
    

# Wedge
for row in range(userinput):
    for col in range(row):
        print(' ', end='')
    for col in range(userinput - row):
        print('x', end='')
    print()
print('-----')


#The Pyramid
for row in range(userinput):
    for col in range (userinput - (row +1)): 
        print(' ', end='')
    for col in range((row * 2) + 1):
        print('x', end='')
    print()
print('-----')


#Empty Square
for row in range(userinput): 
    for col in range(userinput):
        if(row < 1 or row > userinput - 2 or col < 1 or col > userinput -2): 
            print('x', end='')
        else:
            print(' ', end='')
    print()
print('-----')


#Negative Diamond
for row in range(userinput):
    if (row ==0):
        for col in range((userinput * 2) -1):
            print ('x', end='')
    else:
        for col in range(userinput - row):
            print('x', end='')
        for col in range((row * 2)-1): 
            print(' ', end='')
        for col in range(userinput - row):
            print('x', end='')
    print()
for row in range(userinput -1): 
    