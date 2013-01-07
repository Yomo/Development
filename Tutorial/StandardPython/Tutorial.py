'''
Created on 04.01.2013

@author: Timme
'''


def Fibonacci(a, b):
    return b, a+b    

a = 1 
b = 2
p = lambda a,b: 'a:' + str(a) + ' b:' + str(b)  

for i in range(10):
    a,b = Fibonacci(a,b)
    print p(a,b)

    
    
