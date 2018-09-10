def collatz(number):
    if number <= 0:
        print('Number must be a whole, positive integer')
        number = 1
        return number
    elif number % 2 == 0:
        number = number // 2
        print(number)
        return number
    elif number % 2 ==1:
        number = 3 * number + 1
        print(number)
        return number

print('Enter number')
try:
    userNum = int(input())
    while userNum !=1:
        userNum = collatz(userNum)
except ValueError:
    print('Please use an integer')
    
