num = int(input('Enter the number: '))

def factorial(num) :
    if num==1:
        return 1
    else:
        return (num * factorial(num-1))
    
result = factorial(num)

print('The factorial of number {0} is {1}'.format(num, result))

