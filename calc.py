print('enter two numbers')
a = int(input())
b = int(input())

print('enter an operation')
op = input()

if op not in '+-/*%^':
    print('unknown op')

if op == '+':
    print('the sum is', a + b)

if op == '-':
    print('the difference is', a - b)

if op == '/':
    print('the quotient is', a / b)

if op == '*':
    m = 0
    for i in range(a):
        m += b
    print('the product is', m)
    
if op == '%':
    print('a mod b is', a % b)
    
if op == '^':
    print('a power b is', a ** b)