def fibonacci_recur(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recur(n-1) + fibonacci_recur(n-2)
    
    
nth_term = int(input('Enter an integer value: '))

if nth_term <= 0:
    print ('Enter an positive integer: ')
    
else:
    print('Fibonacci sequence'.upper())
    for i in range(nth_term):
        print (fibonacci_recur(i))
    