def fibonacci(n) :
    if n < 1 : 
        return 0
    prev = 0
    curr = 1
    for i in range(n-1) :
        temp = curr
        curr += prev
        prev = temp
    return curr

def golden_ratio(n) :
    if n < 2 : 
        return 1.
    prev = 0
    curr = 1
    for i in range(n) :
        temp = curr
        curr += prev
        prev = temp
    return curr/prev

def wallis_pi(n) :
    result = 2.
    for k in range(1,n+1) :
        result *= (4. * k**2)/(4. * k**2 - 1.)
    return result

def collatz(n) :
    steps = -1
    while n > 0 : # Don't run for negative numbers
        steps += 1
        if n == 1 :
            break
        if n % 2 == 0 :
            n = n // 2
        else :
            n = 3*n +1
    return steps
