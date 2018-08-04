def findFactorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        factorial = num * findFactorial(num -1)
        return factorial

num = input(" Enter the number to find the Factorial: ")
if num < 0:
    print -1
else:
    print "The Factorial is: ",findFactorial(num)

