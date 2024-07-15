num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

def compute_lcm(x,y):
    if (x>y) :
        greater = x
    else:
        greater = y

    while (True):
        if (greater%x==0) and (greater %y==0):
            lcm =  greater
            break

        else:
            greater+=1
    
    return lcm
    
print('The LCM is: ', compute_lcm(num1, num2))


