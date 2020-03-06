# def divisors(num):
#     l = [a for a in range(2,num) if num%a == 0]
#     if len(l) == 0:
#         return str(num) + " is prime"
#     print(l)

# divisors(20)

# def last_digit(num1,num2):
#     exponent= pow(num1 , num2)
#     NewList=[int(x) for x in str(exponent)]
#     print(NewList[-1])

# last_digit(10,10**10)

def alphanumeric(password):
    digits = [0,1,2,3,4,5,6,7,8,9]
    excluded = ["",'_']
    UpperPassWord = password.upper()
    
    NewPassword = list(UpperPassWord)

    for item in digits:
        if str(item) in UpperPassWord:
            print('pass')
        else:
            print('fail')    

alphanumeric("PassW0rd")                        