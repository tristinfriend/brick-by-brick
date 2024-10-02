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

for row in range(userinput):
    for col in range(row+1):
        print('x', end='')
    print()


    