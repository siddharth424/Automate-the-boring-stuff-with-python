def collatz(number):
    if number==1:
        number=1
    elif number%2==0:
        print(number//2)
        collatz(number//2)
    else:
        print(number*3+1)
        collatz(number*3+1)
try:
    collatz(int(input()))
except ValueError:
    print('The entered value is not an integer')
