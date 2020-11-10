
def fact(n):
# base case a simple solution which stops process from recurring
    if n == 1 or n == 0:
        return 1
# recursive case - case when a function calls itself
# in this case it's calling the factorial
    else:
        return n * fact(n-1)
    
print(fact(1))
