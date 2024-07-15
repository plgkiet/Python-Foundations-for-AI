num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

def compute_hcf(x,y):
    if (x<y) :
        smaller = x
    else:
        smaller = y

    while (True):
        if (num1 % smaller == 0) and (num2 % smaller ==0):
            hcf =  smaller
            break

        else:
            smaller-=1
    
    return hcf
    
print('The LCM is: ', compute_hcf(num1, num2))


