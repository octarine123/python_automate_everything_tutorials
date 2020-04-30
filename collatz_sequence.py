print('Enter a number')
x=int(input())

if x < 1:
    print('Please type in an integer larger than 1')
else:
    while x != 1:
        if x % 2 == 0:
            x=3*x + 1
            print(x)
        else:
            x=x//2
            print(x)
